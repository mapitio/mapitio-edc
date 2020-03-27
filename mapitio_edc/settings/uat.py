from multisite import SiteID

from .defaults import *  # noqa

print(f"Settings file {__file__}")  # noqa

SITE_ID = SiteID(default=1)
EDC_SITES_UAT_DOMAIN = True
ALLOWED_HOSTS = [
    "hindu-mandal.uat.tz.mapitio.clinicedc.org",
    "localhost",
]
