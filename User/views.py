from django.contrib.auth.decorators import login_required
from django.core import serializers
from decimal import *
from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils import http
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .models import *

from .forms import *
from .decorator import *

from Administer.models import *



@my_login_required_for_user
def TimecardlistView(request):
    Datadict = serializers.serialize("python", Timecard.objects.all())
    header = 'timecard'
    context = {'Datadict': Datadict, 'header': header}
    return render(request, "User/list.html", context=context)


@method_decorator(my_login_required_for_user, name='dispatch')
class UserTimeCardCreation(CreateView):
    model = UserTimeCard
    form_class = UserTimeCardForm
    template_name = 'User/pleasework.html'
    success_url = reverse_lazy('User:usertimecardlist')


    def get_context_data(self, **kwargs):
        data = super(UserTimeCardCreation,self).get_context_data(**kwargs)
        if self.request.POST:
            data['Laborcosts'] = UserTimeCardLaborFormSet(self.request.POST)
            data['Machinecosts'] = UserTimeCardMachineFormSet(self.request.POST)
        else:
            data['Laborcosts'] = UserTimeCardLaborFormSet()
            data['Machinecosts'] = UserTimeCardMachineFormSet()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        Laborcost = context['Laborcosts']
        Machinecost = context['Machinecosts']
        with transaction.atomic():
            form.instance.created_by=self.request.user

            self.object = form.save()
            if Laborcost.is_valid():
                Laborcost.instance = self.object
                Laborcost.save()
            else:
                return render(self.request,'User/pleasework.html',self.get_context_data())
            if Machinecost.is_valid():
                Machinecost.instance = self.object
                Machinecost.save()


        form.save()
        sitecode = form.cleaned_data['Sitecode']
        name = form.cleaned_data['nameofcontracter']
        totalhrsforlaborsum = 0
        totalamountsumforlabor = 0
        totalhrsformachinesum = 0
        totalamountsumformachines = 0
        for i in Laborcost.cleaned_data:
            hrs = int(i['Totalhrs'])
            cost = convertMoneyStringtoDecimal(i['Totalamount'])
            jobcode = i['JobCode']



            thisjob = Job.objects.get(job=jobcode)
            targetedhours = int(thisjob.MaxHoursPerDay)
            targetrate = convertMoneyStringtoDecimal(thisjob.HourlyRate)

            targetedamount = targetrate * targetedhours



            totalhrsforlaborsum += hrs
            totalamountsumforlabor += (cost)

        for i in Machinecost.cleaned_data:
            hrs = i['Totalhrs']
            cost = i['Totalamount']
            totalhrsformachinesum += int(hrs)
            totalamountsumformachines += convertMoneyStringtoDecimal(cost)

        TOTALHRS = totalhrsformachinesum + totalhrsforlaborsum
        TOTALCOST = totalamountsumformachines + totalamountsumforlabor
        Timecard.objects.create(Sitecode=sitecode, nameofcontracter=name, Totalhrs=TOTALHRS, Totalamount=convertDecimaltoMoney(TOTALCOST))


        return super(UserTimeCardCreation,self).form_valid(form)



    def form_invalid(self, form):
        print('Reached')



def convertMoneyStringtoDecimal(x):
    x = x.replace(",",'')
    x = float(x.replace("$",''))
    return x

def convertDecimaltoMoney(x):
    return '${:,.2f}'.format(x)