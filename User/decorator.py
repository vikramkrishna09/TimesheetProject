from django.http import HttpResponseRedirect
from django.urls import reverse


def my_login_required_for_user(function):
    def wrapper(request, *args, **kw):
        user=request.user
        if user.is_superuser == False and user.is_authenticated == False:
            return HttpResponseRedirect(reverse('home:home'))
        if user.is_superuser == False and user.is_authenticated:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('Admin:admintimecardlist'))
    return wrapper