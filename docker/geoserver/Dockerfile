FROM tomcat:8-jre7

RUN apt-get -y update

RUN apt-get -y install wget unzip

RUN wget -O /usr/local/tomcat/webapps/geoserver.war http://build.geonode.org/geoserver/latest/geoserver.war
RUN apt-get remove -y wget

ENV GEOSERVER_DATA_DIR /opt/geoserver/data_dir

ADD geoserver.xml /usr/local/tomcat/conf/Catalina/localhost/geoserver.xml

EXPOSE 8080
EXPOSE 8090
