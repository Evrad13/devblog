from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBED = 'SUBSCRIBED'

    CHOICE_ROLE = (

        (CREATOR, 'créateur'),

        (SUBSCRIBED, 'abonné'),
    )

    profile_foto = models.ImageField(verbose_name='phote de profile')
    role = models.CharField(max_length=30, choices=CHOICE_ROLE, verbose_name='role utilisateur')
