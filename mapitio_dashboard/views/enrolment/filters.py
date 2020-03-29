from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class ListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(name="all", label="All", lookup={})

    consented = ListboardFilter(
        label="Consented", position=20, lookup={"eligible": True, "consented": True}
    )

    not_consented = ListboardFilter(
        label="Not consented",
        position=21,
        lookup={"eligible": True, "consented": False},
    )
