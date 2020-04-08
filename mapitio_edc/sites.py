from edc_sites.single_site import SingleSite

fqdn = "mapitio.clinicedc.org"

all_sites = {
    "tanzania": [
        SingleSite(
            10,
            "hindu_mandal",
            country="tanzania",
            country_code="tz",
            domain=f"hindu-mandal.tz.{fqdn}",
        ),
    ],
}
