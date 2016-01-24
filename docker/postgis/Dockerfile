FROM postgres:9.4

ENV POSTGIS_MAJOR 2.1

RUN apt-get update && apt-get install -y postgresql-9.4-postgis-2.1

#RUN ./docker-entrypoint.sh postgres
#USER postgres

COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/initdb-postgis.sh
COPY ./geonode_authorize_layer.sql /docker-entrypoint-initdb.d/geonode_authorize_layer.sql
RUN rm -f /var/lib/postgresql/data/postmaster.pid
