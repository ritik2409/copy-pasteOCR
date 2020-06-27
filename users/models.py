from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager


class UserManager(AbstractUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractUser):
    username = models.CharField(db_index=True, max_length=50,verbose_name="username",
                                unique=True)
    email = models.CharField(db_index=True, max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username