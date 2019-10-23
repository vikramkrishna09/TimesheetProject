from django.conf.urls import url

from .views import *
from . import views
app_name = 'User'


urlpatterns = [

    url(r'^Timecard/Create',UserTimeCardCreation.as_view(),name='usercreatetimecard'),
    url(r'^Timecard/List',views.TimecardlistView,name='usertimecardlist')

]