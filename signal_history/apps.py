from django.apps import AppConfig



class SignalHistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_history'

    # def ready(self):
    #     import signal_history.signals
