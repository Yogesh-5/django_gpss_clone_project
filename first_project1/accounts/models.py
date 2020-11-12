from django.db import models
from django.contrib import auth
# Create your models here.
from django.core.exceptions import ValidationError

class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)




def validate_edu_email_address(value):
    if email.endswith('.edu'):
        raise forms.ValidationError("Only .edu email addresses allowed")

class SignUp(models.Model):
    email = models.EmailField(validators=[validate_edu_email_address])
    ...
