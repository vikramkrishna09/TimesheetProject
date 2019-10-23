from django.conf.urls import url

from .views import *
from . import views
app_name = 'Administer'

urlpatterns = [
url(r'^Job/List',
    views.JoblistView,
    name='adminjoblist'),
url(r'^Machine/List',
    views.MachineListView,
    name='adminmachinelist'),
url(r'^Timecard/List',
    views.TimecardlistView,
    name='admintimecardlist'),

url(r'^Job/Create',
    CreateJob.as_view(),
    name='createjob'),
url(r'^Machine/Create',
    CreateMachine.as_view(),
    name='createmachine'),
url(r'^Timecard/Create',
    CreateTimeCard.as_view(),
    name='createtimecard'),

url(r'^Job/Update/(?P<pk>\d+)',
    JobUpdate.as_view(),
    name='updatejob'),

url(r'^Machine/Update/(?P<pk>\d+)',
    MachineUpdate.as_view(),
    name='updatemachine'),

url(r'^Timecard/Update/(?P<pk>\d+)',
    TimecardUpdate.as_view(),
    name='updatetimecard'),

url(r'^Job/Delete/(?P<pk>\d+)',
    JobDelete.as_view(),
    name='deletejob'),

url(r'^Machine/Delete/(?P<pk>\d+)',
    MachineDelete.as_view(),
    name='deletemachine'),

url(r'^Timecard/Delete/(?P<pk>\d+)',
    TimecardDelete.as_view(),
    name='deletetimecard'),
]