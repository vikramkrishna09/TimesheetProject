from django.conf.urls import url

from . import views
from .views import *
app_name = 'home'


from .views import *
urlpatterns = [
    url(r'home',views.homeView,name='homescreen'),
    url(r'login',LoginUser.as_view(),name='login'),
    url(r'logout',views.logout_view,name='logoutscreen')
]