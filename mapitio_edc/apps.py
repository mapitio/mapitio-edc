from django.apps import AppConfig as DjangoAppConfig, apps as django_apps
from django.db.backends.signals import connection_created
from edc_auth.group_permissions_updater import GroupPermissionsUpdater
from edc_utils.sqlite import activate_foreign_keys
from django.db.models.signals import post_migrate


def post_migrate_update_edc_auth(sender=None, **kwargs):
    """Populate groups, roles, etc.

    Be sure to add a `models.py` to the app to trigger the
    post_migrate signal.
    """
    from mapitio_auth.codenames_by_group import get_codenames_by_group

    GroupPermissionsUpdater(
        codenames_by_group=get_codenames_by_group(), verbose=True, apps=django_apps
    )


class AppConfig(DjangoAppConfig):
    name = "mapitio_edc"

    def ready(self):
        post_migrate.connect(post_migrate_update_edc_auth, sender=self)
        # for sqlite only
        connection_created.connect(activate_foreign_keys)


class AppConfigForTests(DjangoAppConfig):
    name = "mapitio_edc"
