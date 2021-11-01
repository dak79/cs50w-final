from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

User._meta.get_field('email')._unique = True
