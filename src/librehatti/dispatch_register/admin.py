from django.contrib import admin
from .models import entry
from .models import Choices
from .forms import dispatch_Form
#from .forms import subject_choices
admin.autodiscover()

# Register your models here.
class DispatchEntry(admin.ModelAdmin):
    list_display=('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')
    search_fields = ['=name_of_Dept_or_Client','=address']
    list_filter = ['dispatch_no', 'name_of_Dept_or_Client']
#    list_select_related = ('name_of_Dept_or_Client','address')
    list_per_page = 20

admin.site.register(entry, DispatchEntry)

class subject_choicesAdmin(admin.ModelAdmin):
    list_display=('description',)
admin.site.register(Choices, subject_choicesAdmin)
