from django.apps import AppConfig


class AccesscodesConfig(AppConfig):
    name = 'accesscodes'

    def ready(self): 
        from . import signals

