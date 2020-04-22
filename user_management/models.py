from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def add_standard_permission(sender, instance, created, **kwargs):
    if Group.objects.filter(name='contributors').exists():
        standard_group = Group.objects.get(name='contributors')
        standard_group.user_set.add(instance)
