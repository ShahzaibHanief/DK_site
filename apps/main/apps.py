from django.apps import AppConfig

class MainConfig(AppConfig):      # ← Changed from MaiConfig to MainConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main'             # ← Changed from 'main' to 'apps.main'