from django import forms
from .models import *
from .views import *

from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_object_layout import *

from Administer.models import *
class UserTimeCardLaborForm(forms.ModelForm):
    class Meta:
        model = UserTimeCardLabor
        fields = '__all__'
        labels = {"Totalhrs": "Total Hours worked",
                  "Totalamount": "Total Amount",

                  "JobCode": "Job code"}


    def clean(self):
        jobcode = self.cleaned_data.get('JobCode')
        thisjob = Job.objects.get(job=jobcode)
        targetedhours = int(thisjob.MaxHoursPerDay)
        targetrate = convertMoneyStringtoDecimal(thisjob.HourlyRate)

        targetedamount = targetrate * targetedhours
        i = self.cleaned_data
        hrs = int(i.get('Totalhrs'))
        cost = convertMoneyStringtoDecimal(i.get('Totalamount'))

        if (hrs > targetedhours):
            raise forms.ValidationError({'Totalhrs':'Invalid hours for the following job code'})

        if (cost>targetedamount):
            raise forms.ValidationError({'Totalamount':'Invalid amount for the following job code'})

        return self.cleaned_data


class UserTimeCardMachineForm(forms.ModelForm):
    class Meta:
        model = UserTimeCardMachine
        fields = '__all__'
        labels = {"Totalhrs": "Total Hours worked",
                  "Totalamount": "Total Amount",
                  "Machinecode": "Machine code"}

UserTimeCardLaborFormSet = inlineformset_factory(UserTimeCard,UserTimeCardLabor,form=UserTimeCardLaborForm,extra=1)
UserTimeCardMachineFormSet = inlineformset_factory(UserTimeCard,UserTimeCardMachine,form=UserTimeCardMachineForm,extra=1)


class UserTimeCardForm(forms.ModelForm):
    class Meta:
        model = UserTimeCard
        fields = '__all__'
        labels = {"Sitecode": "Site code",
                  "nameofcontracter": "Contractor's Name"}


    def __init__(self, *args, **kwargs):
        super(UserTimeCardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('Sitecode'),
                Field('nameofcontracter'),
                Fieldset('Add Labor Costs',
                    Formset('Laborcosts')),
                Fieldset('Add Machine costs',
                         Formset('Machinecosts')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

def convertMoneyStringtoDecimal(x):
    x = x.replace(",",'')
    x = float(x.replace("$",''))
    return x

def convertDecimaltoMoney(x):
    return '${:,.2f}'.format(x)