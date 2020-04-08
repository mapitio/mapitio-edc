from django.apps import AppConfig as DjangoApponfig
from django.db.models.signals import post_migrate
from edc_auth.group_permissions_updater import GroupPermissionsUpdater
from django.apps import apps as django_apps


def post_migrate_update_edc_auth(sender=None, **kwargs):
    """Populate groups, roles, etc.

    Be sure to add a `models.py` to the app to trigger the
    post_migrate signal.
    """
    from mapitio_auth.codenames_by_group import get_codenames_by_group

    GroupPermissionsUpdater(
        codenames_by_group=get_codenames_by_group(), verbose=True, apps=django_apps
    )


class AppConfig(DjangoApponfig):
    name = "mapitio_auth"
    verbose_name = "Mapitio Authentication and Permissions"

    def ready(self):
        post_migrate.connect(post_migrate_update_edc_auth, sender=self)
