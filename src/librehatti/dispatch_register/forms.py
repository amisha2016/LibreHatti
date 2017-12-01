from django import forms
from .models import entry, add_subchoice
#from .models import Choices
from ajax_select import make_ajax_field
from django.forms.widgets import CheckboxSelectMultiple

sub_choices = [
('Freshman', 'Freshman'),
('Sophomore', 'Sophomore'),
('JR', 'Junior'),
('SR', 'Senior'),
]
checking=[(str(o.id), str(o)) for o in add_subchoice.objects.all()]

class dispatch_Form(forms.ModelForm):

    class Meta:
        model = entry
#        fields = ('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')
        fields = ('dispatch_no','date','name_of_Dept_or_Client','address','place','agency')
#        subject = forms.ChoiceField(choices=[(i.id, str(i)) for i in add_subchoice.objects.all()], widget=forms.CheckboxSelectMultiple)
#    choices = forms.ModelChoiceField(queryset=Choices.objects.all())

    def __init__(self, *args, **kwargs):
        super(dispatch_Form, self).__init__(*args, **kwargs)
        self.fields['agency'].required = False
       # self.fields['subject']=forms.ModelMultipleChoiceField(queryset=add_subchoice.objects.all(), widget=forms.CheckboxSelectMultiple)
        self.fields['subject']=forms.MultipleChoiceField(choices=[(str(o.id), str(o)) for o in add_subchoice.objects.all()], widget=forms.CheckboxSelectMultiple)
#        self.fields['subject']=forms.MultipleChoiceField(choices=sub_choices, widget=forms.CheckboxSelectMultiple)


class subjectForm(forms.ModelForm):

#    def __init__(self,, *args, **kwargs):
#        super(dispatch_Form, self).__init__(*args, **kwargs)
#        self.fields['call_name'].required = False
#        subject_choices.sub_choices.append((call_name,readable_name))

#    subje = forms.ModelChoiceField(queryset=subject_choices.objects.all())
#    queryse=subject_choices.objects.all()
#    subject_text = forms.ChoiceField(choices=subject_choices.sub_choices, widget=forms.CheckboxSelectMultiple)
    
#    import ipdb
#    ipdb.set_trace()
    class Meta:
        model = add_subchoice

#import ipdb
#ipdb.set_trace()


#class subject_choices(forms.ModelForm):

#    class Meta:
#        model = Choices
#	field = ('description')


#class ChoicesForm(forms.ModelForm):
#    """
#    Form for selecting staff for team.
#    """

    # staff = forms.ModelChoiceField(queryset=Staff.objects.all())
#    description = make_ajax_field(Choices, 'description', 'description')

#    def __init__(self, *args, **kwargs):
#         super(ChoicesForm, self).__init__(*args, **kwargs)
#         self.fields['description'].widget.attrs={'class':'form-control'}
