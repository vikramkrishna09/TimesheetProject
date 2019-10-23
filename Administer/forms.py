from django.forms import forms,ModelForm,Form
from django import forms
from .models import Job,Machine,Timecard


class JobCreateForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        labels = {"job": "Enter Job Code",
                  "Description": "Enter Job Description",
                  "HourlyRate": "Enter Hourly Rate",
                  "MaxHoursPerDay": "Enter Max Number of Hours"}

Choices = (('Accept', 'Accept'), ('Decline','Decline'))


class TimeCardAcceptForm(ModelForm):

    AcceptorDecline = forms.ChoiceField(choices=Choices,label='Review')
    class Meta:
        model = Timecard
        labels = {'Sitecode': 'Site Code',
                 'nameofcontracter': 'Name of contracter',
                  'Totalhrs': 'Total Hours',
                   'Totalamount': 'Total Amount',

                  }
        exclude = ('State',)
    def __init__(self,*args,**kwargs):
        super(TimeCardAcceptForm,self).__init__(*args,**kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['Sitecode'].widget.attrs['readonly']=True
            self.fields['nameofcontracter'].widget.attrs['readonly']=True
            self.fields['Totalhrs'].widget.attrs['readonly']=True
            self.fields['Totalamount'].widget.attrs['readonly']=True

class MachineCreateForm(ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'
        labels = {"machinecode": "Enter Machine Code",
                  "Description": "Enter Machine Description",
                  "HourlyRate": "Enter Hourly Rate",
                  "MaxHoursPerDay": "Enter Max Number of Hours"}

class TimecardCreateForm(ModelForm):
    class Meta:
        model = Timecard
        fields = '__all__'

