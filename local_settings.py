import os
import geonode
import datetime

SITENAME = 'Geonode'
SITEURL = 'http://192.168.99.100/'
SITE_ID = 1
GEOSERVER_URL = SITEURL + '/geoserver/'
GEOSERVER_BASE_URL = GEOSERVER_URL
MEDIA_ROOT = '/var/www/geonode/uploaded/'
STATIC_ROOT = '/var/www/geonode/static/'
# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
'default': {
'BACKEND': 'geonode.geoserver',
'LOCATION': 'http://http://192.168.99.100:80/geoserver/', # Docker IP
'PUBLIC_LOCATION': GEOSERVER_URL,
'USER': 'admin',
'PASSWORD': 'admin',
'MAPFISH_PRINT_ENABLED': True,
'PRINT_NG_ENABLED': True,
'GEONODE_SECURITY_ENABLED': True,
'GEOGIT_ENABLED': False,
'WMST_ENABLED': False,
'BACKEND_WRITE_ENABLED': True,
'WPS_ENABLED': True,
# Set to name of database in DATABASES dictionary to enable
'DATASTORE': 'datastore',
}
}
POSTGIS_VERSION = (2, 1, 0)

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'geonode',
'USER': 'geonode',
'PASSWORD': 'geonode',
'HOST': 'postgis',
'PORT': 5432,
},
'datastore': {
'ENGINE': 'django.contrib.gis.db.backends.postgis',
'NAME': 'geonode-imports',
'USER': 'geonode',
'PASSWORD': 'geonode',
'HOST': 'postgis',
'PORT': 5432,
}
}

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings
ALLOWED_HOSTS=['*', 'localhost']
PROXY_ALLOWED_HOSTS=['*', 'localhost']
REGISTRATION_OPEN = True
GEONODE_ROOT = os.path.dirname(geonode.__file__)
STATICFILES_DIRS = [
    os.path.join(GEONODE_ROOT, 'static'),
]
BING_API_KEY = ''
