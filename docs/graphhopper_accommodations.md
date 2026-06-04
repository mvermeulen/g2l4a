# Investigation: GraphHopper Location Precision & Accommodation Overlays

This report addresses how to bypass general city centers to use precise coordinate-level locations in the routing engine, and outlines how to integrate hotel and campsite information overlays for route recommendations.

---

## 1. Precise Coordinate-Level Locations in GraphHopper

### GraphHopper Capabilities
GraphHopper routes between spatial coordinates (latitude and longitude) rather than city names. The underlying engine accepts double-precision float inputs. 
In `g2l4a`, coordinates are rounded to **6 decimal places** in the database cache. This provides an accuracy of **~11 centimeters**, which is more than sufficient for routing to:
* Exact street addresses
* Specific hotel entrances
* Trailheads and campgrounds
* Custom POIs (Points of Interest)

### Code Limitations in `g2l4a`
The limitation is in how inputs are parsed in `src/validation.py`. The `RequestParser` only supports:
1. Strings (which it checks against the hardcoded `CITY_REGISTRY` or queries Nominatim/Open-Meteo online geocoding).
2. Dictionaries specifying a `name` and optional `rest_days` (which it then resolves using the same geocoding pipeline).

### Proposed Solution: Direct Coordinate Inputs
We can extend `RequestParser` in `src/validation.py` to allow:
1. **Explicit Coordinates in YAML Dictionaries**:
   ```yaml
   start_city:
     name: "Austin Hostel"
     latitude: 30.2672
     longitude: -97.7431
     rest_days: 1
   ```
2. **Inline Coordinates in Strings**:
   ```yaml
   via_cities:
     - "30.2672,-97.7431"
     - "Tallahassee, Florida"
   ```

#### Implementation Plan for `src/validation.py`
Modify `extract_city_info` and `_resolve_city` to check if coordinates are provided directly:
```python
# Inside _resolve_city:
if isinstance(name_or_payload, dict) and "latitude" in name_or_payload and "longitude" in name_or_payload:
    return City(
        name=name_or_payload.get("name", "Custom Location"),
        latitude=float(name_or_payload["latitude"]),
        longitude=float(name_or_payload["longitude"]),
        rest_days=name_or_payload.get("rest_days", 0)
    )
```

---

## 2. Accommodation Overlays (Hotels, Hostels & Campsites)

To overlay lodging information onto the generated daily schedules (for rest days and travel stopovers), we can introduce an `AccommodationProvider` interface.

### Option A: OpenStreetMap Overpass API (Recommended)
The **Overpass API** is a read-only OSM query service that allows filtering spatial features by tag and bounding box/radius.
* **Query Type**:
  Query OSM elements with tags like `tourism=hotel`, `tourism=hostel`, `tourism=motel`, or `tourism=camp_site` within $N$ miles of a daily stopover coordinate.
* **Example Overpass Query (JSON)**:
  ```ql
  [out:json][timeout:10];
  (
    node["tourism"~"hotel|hostel|camp_site"](around:5000, 30.2672, -97.7431);
    way["tourism"~"hotel|hostel|camp_site"](around:5000, 30.2672, -97.7431);
  );
  out body;
  ```
* **Pros**:
  * Free, open-source, and does not require API keys or developer registrations.
  * Captures specialized bike-touring accommodations (wild campsites, state parks, and hostels) that commercial APIs omit.
* **Cons**:
  * Does not contain price, live availability, or booking links.

### Option B: Google Places API (Lodging Type)
Queries the Google Maps database using text or coordinate search.
* **Query Type**:
  Use the Place Search API with `location=lat,lon`, `radius=5000`, and `type=lodging`.
* **Pros**:
  * Unparalleled coverage of commercial hotels, motels, B&Bs, and ratings.
* **Cons**:
  * Requires a billing-enabled Google Cloud account and API key.
  * Expensive for high-throughput batch queries.

### Option C: Booking.com / TripAdvisor APIs
Connects directly to reservation databases.
* **Query Type**:
  Search for properties near coordinates with input dates.
* **Pros**:
  * Real-time pricing, availability, and direct booking links.
* **Cons**:
  * Closed APIs; obtaining developer access keys requires corporate approval and commercial partnerships.

---

## 3. Integration Design into `g2l4a`

To display these accommodations in output reports:

1. **Add Accommodation Provider Interface**:
   ```python
   # src/providers.py
   class AccommodationProvider(ABC):
       @abstractmethod
       def get_nearby_accommodations(self, lat: float, lon: float, radius_miles: float) -> List[Dict[str, Any]]:
           pass
   ```
2. **Create Overpass Implementation**:
   Implement `OverpassAccommodationProvider` to query a public Overpass interpreter endpoint (e.g. `https://overpass-api.de/api/interpreter`).
3. **Extend Config**:
   ```yaml
   accommodation_overlay:
     enabled: true
     provider: "overpass"
     radius_miles: 5.0
     max_results: 5
     types: ["hotel", "hostel", "camp_site"]
   ```
4. **Enforce Caching**:
   Save geocoded accommodations in `SQLiteCacheManager` inside a new `accommodation_cache` table to avoid repeating network calls on subsequent solver runs.
5. **Output in Reports**:
   Include a list of recommended options inside the daily travel schedule tables or in a dedicated "Lodging Suggestions" section in the markdown/JSON reports.
