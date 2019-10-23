from django.contrib.auth.models import User
from django.forms import *


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = {'username','password'}

