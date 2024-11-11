from django.apps import AppConfig


class VitalEventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vital_events'

    def ready(self):
        import vital_events.signals