from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .forms import *
from .models import Job,Machine,Timecard
from .urls import *
from django.contrib.auth.decorators import login_required

from django_tables2 import SingleTableView

from django.core import serializers
from django.forms.models import model_to_dict

from django.urls import reverse_lazy
from .decorator import *
# Create your views here.



@my_login_required
def JoblistView(request):
        Datadict = serializers.serialize("python", Job.objects.all())
        header = 'job'
        context = {'Datadict':Datadict,'header':header}
        return render(request, "Administer/list.html", context=context)

@my_login_required
def MachineListView(request):
        Datadict = serializers.serialize("python", Machine.objects.all())
        header = 'machine'

        context = {'Datadict': Datadict,'header':header}
        return render(request, "Administer/list.html", context=context)


@my_login_required
def TimecardlistView(request):
        Datadict = serializers.serialize("python", Timecard.objects.all())
        header = 'timecard'

        context = {'Datadict': Datadict, 'header': header}
        return render(request, "Administer/list.html", context=context)







@method_decorator(my_login_required, name='dispatch')
class CreateJob(CreateView):
    template_name = 'Administer/create.html'
    form_class = JobCreateForm



    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateJob, self).form_valid(form)

@method_decorator(my_login_required, name='dispatch')

class CreateMachine(CreateView):
    template_name = 'Administer/create.html'
    form_class = MachineCreateForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMachine, self).form_valid(form)

class CreateTimeCard(CreateView):
    template_name = 'Administer/create.html'
    form_class = TimecardCreateForm
@method_decorator(my_login_required, name='dispatch')

class JobUpdate(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'Administer/create.html'
@method_decorator(my_login_required, name='dispatch')

class MachineUpdate(UpdateView):
    model = Machine
    fields = '__all__'
    template_name = 'Administer/create.html'
@method_decorator(my_login_required, name='dispatch')



class TimecardUpdate(UpdateView):
    model = Timecard
    template_name = 'Administer/create.html'
    form_class = TimeCardAcceptForm

    def form_valid(self, form):
        State = form.cleaned_data['AcceptorDecline']

        timec = self.object
        if(State == 'Accept'):
            timec.State = 'Accepted'
        else:
            timec.State = 'Declined'
        print(State)
        self.object = timec

        return super().form_valid(form)

@method_decorator(my_login_required, name='dispatch')

class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('Administer:adminjoblist')
    def get(self, request, *args, **kwargs):
        return self.delete(request,args,kwargs)
@method_decorator(my_login_required, name='dispatch')

class MachineDelete(DeleteView):
    model = Machine
    success_url = reverse_lazy('Administer:adminmachinelist')
    def get(self, request, *args, **kwargs):
        return self.delete(request,args,kwargs)
@method_decorator(my_login_required, name='dispatch')

class TimecardDelete(DeleteView):
    model = Timecard
    success_url = reverse_lazy('Administer:admintimecardlist')
    def get(self, request, *args, **kwargs):
        return self.delete(request,args,kwargs)


"""
Old Functions


"""
class Joblist(ListView):
    queryset = Job.objects.values()

    template_name = 'Administer/joblist.html'
    context_object_name = 'Data'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['Datadict'] = serializers.serialize("python", Job.objects.all())
        return data

class MachineList(ListView):
    queryset = Machine.objects.all()
    context_object_name = 'Data'
    template_name = 'Administer/machinelist.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['Datadict'] = serializers.serialize("python", Machine.objects.all())
        return data

class TimecardList(ListView):
    queryset = Timecard.objects.all()
    context_object_name = 'Data'
    template_name = 'Administer/timecardlist.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['Datadict'] = serializers.serialize("python", Timecard.objects.all())
        return data
