from django import forms
from .models import entry, sub_choices, remark_choices
from ajax_select import make_ajax_field
from django.forms.widgets import CheckboxSelectMultiple

class dispatch_Form(forms.ModelForm):

    name_of_Dept_or_Client=make_ajax_field(entry, 'name_of_Dept_or_Client', 'buyer')
    class Meta:
        model = entry

    def __init__(self, *args, **kwargs):
        super(dispatch_Form, self).__init__(*args, **kwargs)
        self.fields['agency'].required = False
        self.fields['subject']=forms.ModelMultipleChoiceField(queryset=sub_choices.objects.all(), widget=forms.CheckboxSelectMultiple)
        self.fields['remarks']=forms.ModelMultipleChoiceField(queryset=remark_choices.objects.all(), widget=forms.CheckboxSelectMultiple)

class subjectForm(forms.ModelForm):

    class Meta:
        model = sub_choices

class remarksForm(forms.ModelForm):

    class Meta:
        model = remark_choices
