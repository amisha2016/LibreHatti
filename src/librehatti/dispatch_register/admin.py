from django.contrib import admin
from .models import entry
from .models import sub_choices, remark_choices
from .forms import dispatch_Form, subjectForm, remarksForm
#from .forms import ChoicesForm
admin.autodiscover()

# Register your models here.


class subject_choicesAdmin(admin.ModelAdmin):
    form = subjectForm
    model=sub_choices
#    extra = 1
    #fields = ['subject_text',]
#    list_display=('description',)

class remarks_choicesAdmin(admin.ModelAdmin):
    form = remarksForm
    model=remark_choices


class DispatchEntry(admin.ModelAdmin):
#    list_display=('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')
    list_display=('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','another')
    search_fields = ['=name_of_Dept_or_Client','=address']
    list_filter = ['dispatch_no', 'name_of_Dept_or_Client']
#    list_select_related = ('name_of_Dept_or_Client','address')
    list_per_page = 20
#    inlines = [subject_choicesAdmin]


admin.site.register(sub_choices, subject_choicesAdmin)
admin.site.register(entry, DispatchEntry)
admin.site.register(remark_choices, remarks_choicesAdmin)


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
