from datetime import date
import pytest
from src.domain import City, Itinerary, DailySchedule, Leg, Scores
from src.scoring import ScoringEngine, haversine_distance, compute_geodesic_baseline

@pytest.fixture
def base_config():
    return {
        "scoring": {
            "weights": {
                "weather": 0.40,
                "distance": 0.40,
                "hills": 0.20
            },
            "comfort": {
                "ideal_temp_f": 70.0,
                "temp_tolerance_f": 20.0
            }
        },
        "daily_constraints": {
            "max_climb_ft_per_day": 4000.0
        }
    }

@pytest.fixture
def engine(base_config):
    return ScoringEngine(base_config)

def test_haversine_and_baseline():
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=30.0, longitude=-91.0)
    
    # Approx 60 miles for 1 degree difference at lat 30
    dist = haversine_distance(c1, c2)
    assert 55.0 <= dist <= 65.0
    
    it = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[]
    )
    base_dist = compute_geodesic_baseline(it)
    assert base_dist == dist

def test_scoring_weather_comfort(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    # 1. Perfect 70 degrees temperature
    it_perfect = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1, date=date(2026, 6, 1),
                origin=c1, destination=c2,
                distance_miles=40.0, ascent_feet=100.0,
                high_temp_f=70.0, low_temp_f=50.0
            )
        ]
    )
    
    score_p = engine.compute_weather_score(it_perfect)
    assert score_p == 1.0

    # 2. Maximum variance (50 degrees or 90 degrees) -> 0.0
    it_bad = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1, date=date(2026, 6, 1),
                origin=c1, destination=c2,
                distance_miles=40.0, ascent_feet=100.0,
                high_temp_f=90.0, low_temp_f=70.0
            )
        ]
    )
    score_b = engine.compute_weather_score(it_bad)
    assert score_b == 0.0

    # 3. Intermediate variance (80 degrees) -> 0.5
    it_mid = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        schedule=[
            DailySchedule(
                day_number=1, date=date(2026, 6, 1),
                origin=c1, destination=c2,
                distance_miles=40.0, ascent_feet=100.0,
                high_temp_f=80.0, low_temp_f=60.0
            )
        ]
    )
    score_m = engine.compute_weather_score(it_mid)
    assert score_m == 0.5

def test_scoring_distance_detour(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=30.0, longitude=-91.0) # baseline dist is approx 60.0 miles
    
    # 1. Exact geodesic path -> 1.0
    it_perfect = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        legs=[
            Leg(origin=c1, destination=c2, distance_miles=compute_geodesic_baseline(Itinerary(c1, c2, [])), ascent_feet=100.0)
        ]
    )
    score_p = engine.compute_distance_score(it_perfect)
    assert score_p == 1.0

    # 2. Path with double distance -> 0.25 (quadratic)
    it_detour = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        legs=[
            Leg(origin=c1, destination=c2, distance_miles=compute_geodesic_baseline(Itinerary(c1, c2, [])) * 2.0, ascent_feet=100.0)
        ]
    )
    score_d = engine.compute_distance_score(it_detour)
    assert score_d == 0.25

def test_scoring_hills_burden(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=31.0, longitude=-91.0)
    
    # 1. Flat path (0 ascent) -> 1.0
    it_flat = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        legs=[
            Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=0.0)
        ]
    )
    score_f = engine.compute_hills_score(it_flat)
    assert score_f == 1.0

    # 2. Climb at maximum constraint cap (4000.0 ft) -> 0.0
    it_climb = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        legs=[
            Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=4000.0)
        ]
    )
    score_c = engine.compute_hills_score(it_climb)
    assert score_c == 0.0

    # 3. Intermediate climb (2000.0 ft) -> 0.5
    it_mid = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        legs=[
            Leg(origin=c1, destination=c2, distance_miles=50.0, ascent_feet=2000.0)
        ]
    )
    score_m = engine.compute_hills_score(it_mid)
    assert score_m == 0.5

def test_scoring_engine_weighted_sum(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=30.0, longitude=-91.0)
    
    # Perfect weather (1.0), perfect distance (1.0), half climb (0.5)
    # Weights: weather 0.40, distance 0.40, hills 0.20
    # Expected: 0.40*1.0 + 0.40*1.0 + 0.20*0.5 = 0.4 + 0.4 + 0.1 = 0.90
    it = Itinerary(
        start_city=c1,
        completion_city=c2,
        via_cities=[],
        legs=[
            Leg(origin=c1, destination=c2, distance_miles=compute_geodesic_baseline(Itinerary(c1, c2, [])), ascent_feet=2000.0)
        ],
        schedule=[
            DailySchedule(
                day_number=1, date=date(2026, 6, 1),
                origin=c1, destination=c2,
                distance_miles=compute_geodesic_baseline(Itinerary(c1, c2, [])), ascent_feet=2000.0,
                high_temp_f=70.0, low_temp_f=50.0
            )
        ]
    )
    
    scored = engine.score_itinerary(it)
    assert scored.scores.weather == 1.0
    assert scored.scores.distance == 1.0
    assert scored.scores.hills == 0.5
    assert scored.scores.total == 0.90

def test_stable_ranking_and_tie_breakers(engine):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=30.0, longitude=-91.0)
    
    # Create three itineraries:
    # it1: Perfect total (0.90)
    it1 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[City(name="X", latitude=30.5, longitude=-90.5)],
        legs=[Leg(origin=c1, destination=c2, distance_miles=60.0, ascent_feet=2000.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=60.0, ascent_feet=2000.0, high_temp_f=70.0, low_temp_f=50.0)]
    )
    
    # it2: Poorer total (lower weather, same miles/climb)
    it2 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[City(name="Y", latitude=30.5, longitude=-90.5)],
        legs=[Leg(origin=c1, destination=c2, distance_miles=60.0, ascent_feet=2000.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=60.0, ascent_feet=2000.0, high_temp_f=80.0, low_temp_f=60.0)]
    )
    
    # it3: Tie on total score with it2 (exact same scores), but shorter distance
    it3 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[City(name="Z", latitude=30.5, longitude=-90.5)],
        legs=[Leg(origin=c1, destination=c2, distance_miles=55.0, ascent_feet=2000.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=55.0, ascent_feet=2000.0, high_temp_f=80.0, low_temp_f=60.0)]
    )

    ranked = engine.rank_itineraries([it2, it1, it3])
    
    # First: it1 (highest total: 0.90)
    assert ranked[0] == it1
    
    # Second: it3 (tied total with it2, but shorter distance 55 miles vs 60 miles)
    assert ranked[1] == it3
    assert ranked[2] == it2

def test_sensitivity_weight_shifting(base_config):
    c1 = City(name="A", latitude=30.0, longitude=-90.0)
    c2 = City(name="B", latitude=30.0, longitude=-91.0)
    
    # Route 1: Shorter distance, extreme weather (total miles=60, temp=90)
    r1 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        legs=[Leg(origin=c1, destination=c2, distance_miles=60.0, ascent_feet=100.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=60.0, ascent_feet=100.0, high_temp_f=90.0, low_temp_f=70.0)]
    )
    
    # Route 2: Detour distance, comfortable weather (total miles=120, temp=70)
    r2 = Itinerary(
        start_city=c1, completion_city=c2, via_cities=[],
        legs=[Leg(origin=c1, destination=c2, distance_miles=120.0, ascent_feet=100.0)],
        schedule=[DailySchedule(day_number=1, date=date(2026, 6, 1), origin=c1, destination=c2, distance_miles=120.0, ascent_feet=100.0, high_temp_f=70.0, low_temp_f=50.0)]
    )

    # Scenario A: Distance-weighted heavy config (dist weight = 0.80, weather weight = 0.10)
    conf_a = dict(base_config)
    conf_a["scoring"]["weights"] = {"weather": 0.10, "distance": 0.80, "hills": 0.10}
    engine_a = ScoringEngine(conf_a)
    
    ranked_a = engine_a.rank_itineraries([r1, r2])
    # Dist favored: r1 (distance score 1.0) should outrank r2 (distance score 0.5)
    assert ranked_a[0] == r1

    # Scenario B: Weather-weighted heavy config (dist weight = 0.10, weather weight = 0.80)
    conf_b = dict(base_config)
    conf_b["scoring"]["weights"] = {"weather": 0.80, "distance": 0.10, "hills": 0.10}
    engine_b = ScoringEngine(conf_b)
    
    ranked_b = engine_b.rank_itineraries([r1, r2])
    # Weather favored: r2 (weather score 1.0) should outrank r1 (weather score 0.0)
    assert ranked_b[0] == r2
