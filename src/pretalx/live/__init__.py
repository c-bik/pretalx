from django.apps import AppConfig


class LiveConfig(AppConfig):
    name = "pretalx.live"

    def ready(self):
        # from . import permissions  # noqa
        # from .phrases import LivePhrases  # noqa
        pass


default_app_config = "pretalx.live.LiveConfig"
