from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServiceAuthConfig(AppConfig):
    name = "service_auth"
    verbose_name = _("Service Authentication")
