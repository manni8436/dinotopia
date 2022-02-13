from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ blog config class """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
