from copy import copy

from edc_auth.codenames import pii as default

pii = copy(default)
pii.remove("mapitio_consent.add_subjectconsent")
pii.remove("mapitio_consent.change_subjectconsent")
pii.remove("mapitio_consent.delete_subjectconsent")
