from django import forms
from .models import entry

class dispatch_Form(forms.ModelForm):

    class Meta:
        model = entry
        fields = ('name', 'agency','address','place','subject','remarks')

    def __init__(self, *args, **kwargs):
        super(dispatch_Form, self).__init__(*args, **kwargs)
        self.fields['agency'].required = False
#class dispatch_Form(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)
