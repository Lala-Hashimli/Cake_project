from django.apps import AppConfig


class CakesConfig(AppConfig):
    name = 'cakes'
    default_auto_field = "django.db.models.BigAutoField"
    
    def ready(self):
        import cakes.signals


