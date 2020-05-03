from copy import copy
from edc_auth import screening as default

default += [
    "mapitio_screening.add_subjectscreening",
    "mapitio_screening.add_subjectrefusal",
    "mapitio_screening.change_subjectscreening",
    "mapitio_screening.change_subjectrefusal",
    "mapitio_screening.delete_subjectscreening",
    "mapitio_screening.delete_subjectrefusal",
    "mapitio_screening.view_historicalsubjectscreening",
    "mapitio_screening.view_historicalsubjectrefusal",
    "mapitio_screening.view_subjectscreening",
    "mapitio_screening.view_subjectrefusal",
]

screening = copy(default)
