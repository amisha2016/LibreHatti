from django import forms
from .models import entry
from .models import Choices
from ajax_select import make_ajax_field

class dispatch_Form(forms.ModelForm):

    class Meta:
        model = entry
        fields = ('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')

    def __init__(self, *args, **kwargs):
        super(dispatch_Form, self).__init__(*args, **kwargs)
        self.fields['agency'].required = False

#class subject_choices(forms.ModelForm):

#    class Meta:
#        model = Choices
#	field = ('description')


class ChoicesForm(forms.ModelForm):
    """
    Form for selecting staff for team.
    """
    # staff = forms.ModelChoiceField(queryset=Staff.objects.all())
    description = make_ajax_field(Choices, 'description', 'description')

    def __init__(self, *args, **kwargs):
         super(ChoicesForm, self).__init__(*args, **kwargs)
         self.fields['description'].widget.attrs={'class':'form-control'}

