from django.contrib import admin
from .models import entry
from .forms import dispatch_Form
admin.autodiscover()

# Register your models here.
class DispatchEntry(admin.ModelAdmin):
    list_display=('dispatch_no','date','name_of_Dept_or_Client','address','place','agency','subject','remarks')
 #   search_fields = ['name']
admin.site.register(entry, DispatchEntry)

