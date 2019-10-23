from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
# Create your views here.


def homeView(request):
    return render(request,'home/kappa.html')



class LoginUser(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                url = reverse('Administer:adminjoblist')
                return url
            else:
                url = reverse('User:usertimecardlist')
                return url


def logout_view(request):
    logout(request)
    context = {'State':'LogOut'}
    return redirect('home:homescreen')

