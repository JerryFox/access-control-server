from registration.signals import user_activated
from django.dispatch import receiver

@receiver(user_activated)
def my_callback(sender, **kwargs):
    print("User activated!")

