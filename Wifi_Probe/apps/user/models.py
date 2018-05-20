from django.db import models
from django.contrib.auth.models import AbstractUser
from tools.validators import *


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     sno = models.CharField(db_column='Sno', max_length=12)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=11)  # Field name made lowercase.
#     mac = models.CharField(db_column='Mac', max_length=20)  # Field name made lowercase.

class User(AbstractUser):

    username = models.CharField(
        db_column='username',
        max_length=12,
        unique=True,
        help_text='Required. Your student No. or staff No.',
        validators=[sno_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    phone = models.CharField(
        db_column='Phone',
        validators=[phone_no_validator],
        max_length=11,
    )
    mac = models.CharField(
        db_column='Mac',
        validators=[mac_address_validator],
        max_length=20,
    )
    is_teacher = models.BooleanField(
        'teacher status',
        default=False,
        help_text='Designates whether the user can create a course.',
    )
