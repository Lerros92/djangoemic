from django import forms
from .models import receiveTable, item
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class AddForm(forms.ModelForm):

    class Meta:
        model = receiveTable
        fields = "__all__"
        labels = {
            "noteNumber": _("So phieu"),
        }

class AddItemForm(forms.ModelForm):

    class Meta:
        model = item
        fields = "__all__"
        widgets = {
            'deadline': DateInput()
        }