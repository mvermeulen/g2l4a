FROM eclipse-temurin:21-jre

WORKDIR /opt/graphhopper

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY docker/graphhopper/entrypoint.sh /usr/local/bin/graphhopper-entrypoint.sh
RUN chmod +x /usr/local/bin/graphhopper-entrypoint.sh

EXPOSE 8989

ENTRYPOINT ["/usr/local/bin/graphhopper-entrypoint.sh"]
