from django.contrib import admin
from .models import entry
from .models import sub_choices, remark_choices
from .forms import dispatch_Form, subjectForm, remarksForm
from librehatti.catalog.forms import BuyerForm
from ajax_select.admin import AjaxSelectAdmin

admin.autodiscover()

class subject_choicesAdmin(admin.ModelAdmin):
    form = subjectForm
    model=sub_choices

class remarks_choicesAdmin(admin.ModelAdmin):
    form = remarksForm
    model=remark_choices

class DispatchEntry(AjaxSelectAdmin):
    form = dispatch_Form
    list_display=('dispatch_no','date','name_of_Dept_or_Client','agency', 'Subjects', 'Remarks')
    search_fields = ['=name_of_Dept_or_Client','=address']
    list_filter = ['dispatch_no', 'name_of_Dept_or_Client']
    list_per_page = 20

    def Subjects(self, obj):
        return ", ".join([subject.readable_name for subject in obj.subject.all()])

    def Remarks(self, obj):
        return ", ".join([remark.readable_name for remark in obj.remarks.all()])

admin.site.register(sub_choices, subject_choicesAdmin)
admin.site.register(entry, DispatchEntry)
admin.site.register(remark_choices, remarks_choicesAdmin)
