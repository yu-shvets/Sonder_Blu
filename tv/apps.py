from django.apps import AppConfig


class TvConfig(AppConfig):
    name = 'tv'

    def ready(self):
        import tv.signals
