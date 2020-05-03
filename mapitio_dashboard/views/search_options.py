import re

from django.db.models import Q


def extra_search_options(search_term):

    q_objects = []

    if re.match("^[A-Z\-]+$", search_term):
        q_objects.append(
            Q(initials__exact=search_term.upper())
            | Q(first_name__exact=search_term.upper())
            | Q(last_name__exact=search_term.upper())
        )
    if re.match("^[A-Z0-9\-]+$", search_term):
        search_term.replace("-", "").upper()
        q_objects.append(
            Q(hospital_identifier__exact=search_term)
            | Q(ctc_identifier__exact=search_term)
            | Q(file_number__exact=search_term)
            | Q(screening_identifier__icontains=search_term)
            | Q(subject_identifier__icontains=search_term)
        )
    return q_objects
