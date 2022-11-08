from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # this is suggested by django to make users/signals.py to work -tian
        import users.signals
