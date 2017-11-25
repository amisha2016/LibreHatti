from django import forms
from .models import entry

class dispatch_Form(forms.ModelForm):

    class Meta:
        model = entry
        fields = ('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')

    def __init__(self, *args, **kwargs):
        super(dispatch_Form, self).__init__(*args, **kwargs)
        self.fields['agency'].required = False
