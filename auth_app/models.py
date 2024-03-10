from django.db import models
from django.contrib.auth.models import AbstractUser

from auth_app.manager import CustomUserManager

# Using our own custom made model.
"""
The DIFFERENCE:
AbstractUser:
In order to make our custom user model we can inherit and extend from this class
and can also add extra fields to our custom model, i.e we do not need to create
anything from scratch.
This class actually provides pre-existing fields and methods that we can use and also
we can create those in our model.
Say, AbstractUser provides all the fields (like, username, password, email, etc.) and we can use those fields
or can create extra fields(like phone_number, age, date_of_birth, etc.) according to our needs.
Those custom defined fields will seamlessly integrate with the those pre-existing fields in AbstractUser
class.

AbstractBaseUser:
We shall extend this class only when we want to create each and every fields from
scratch.
This class does not provide any pre-existing fields(other than username and password)
and we can add our own fields.

"""


# In this scenario, we'll be using the AbstractUser class.


class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=True)

    """
    We need to set the USERNAME_FIELD to 'email' because we want to use
    that field instead of username(which is set to None in this case).
    """
    USERNAME_FIELD = "email"
    """
    All fields other than the one set in USERNAME_FIELD need to be 
    set in REQUIRED_FIELDS.
    """
    REQUIRED_FIELDS = ["phone_number"]

    # As we are creating our own custom model we also need to create
    # our own custom model manager and add it as
    """objects -> CustomUserManager"""
    objects = CustomUserManager()

    def __str__(self):
        return self.email
