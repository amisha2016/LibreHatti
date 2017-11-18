from django.contrib import admin
from .models import entry
from .forms import dispatch_Form
admin.autodiscover()

# Register your models herei.
class hello(admin.ModelAdmin):
    list_display=('id','pub_date','name','agency','address','place','subject','remarks')

admin.site.register(entry,hello)

