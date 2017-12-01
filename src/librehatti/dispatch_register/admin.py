from django.contrib import admin
from .models import entry
from .models import add_subchoice
from .forms import dispatch_Form, subjectForm
#from .forms import ChoicesForm
admin.autodiscover()

# Register your models here.


class subject_choicesAdmin(admin.ModelAdmin):
    form = subjectForm
    model=add_subchoice
#    extra = 1
    #fields = ['subject_text',]
#    list_display=('description',)

class DispatchEntry(admin.ModelAdmin):
    list_display=('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')
    list_display=('dispatch_no','date','name_of_Dept_or_Client','address','place','agency')
    search_fields = ['=name_of_Dept_or_Client','=address']
    list_filter = ['dispatch_no', 'name_of_Dept_or_Client']
#    list_select_related = ('name_of_Dept_or_Client','address')
    list_per_page = 20
#    inlines = [subject_choicesAdmin]


#admin.site.register(Choices, subject_choicesAdmin)
admin.site.register(entry, DispatchEntry)
admin.site.register(add_subchoice, subject_choicesAdmin)


class StaffInl(admin.StackedInline):
    """
    This class is used to add, edit or delete staff.
    """
#    form = ChoicesForm
#    model = Choices
#    fields = ['description', ]
#    extra = 3
#admin.site.register(subject_choices, subject_choicesAdmin)
#import ipdb
#ipdb.set_trace()
