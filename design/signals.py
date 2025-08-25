from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Voter

@receiver(post_save,sender=User)

def create_voter_for_new_voter(sender,instance,created,**kwargs):
    if created:
        Voter.objects.create(user=instance)
    