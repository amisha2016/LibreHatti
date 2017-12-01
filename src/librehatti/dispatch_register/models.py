from django.db import models

import useraccounts

from librehatti.catalog.models import Product
from librehatti.catalog.models import ModeOfPayment
from librehatti.catalog.models import Surcharge
from django.utils import timezone
from django.contrib.auth.models import User

from librehatti.config import _BUYER
from librehatti.config import _DELIVERY_ADDRESS
from librehatti.config import _IS_DEBIT
from librehatti.config import _PURCHASED_ITEMS
from librehatti.config import _QTY
from librehatti.config import _REFERENCE
from librehatti.config import _REFERENCE_DATE

from librehatti.voucher.models import FinancialSession

from django.core.urlresolvers import reverse

class add_subchoice(models.Model):
 #   choice=models.ForeignKey(entry)
    call_name=models.CharField(max_length=200)
    readable_name=models.CharField(max_length=200)
#    sub_choices=[]
#    sub_choices.append((self.objects.values_list('call_name'),(self.objects.values_list('readable_name')))
    def __str__(self):
        return self.call_name



class entry(models.Model):
    """
    Handling dispatch register
    """
    dispatch_no = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    name_of_Dept_or_Client = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    agency = models.CharField(max_length=200, blank=True)
#    subject = models.CharField(max_length=200, choices=add_subchoice.sub_choices, default='qwer')
    subject = models.CharField(max_length=200,choices=[(str(o.id), str(o)) for o in add_subchoice.objects.all()], default='doit')
#    subject = models.CharField(max_length=200,choices=[(o.id, str(o)) for o in add_subchoice.objects.all()], default='doit')

#    remarks = models.CharField(max_length=200)

   # def __str__(self):
#        return self.name_of_Dept_or_Client
   # def __iter__(self):
#        return self.objects.values_list('subject_text')
#        return [self.subject_text]



#class subject_choices(models.Model):
#    sub_choices = [
#        ('Freshman', 'Freshman'),
#        ('Sophomore', 'Sophomore'),
#        ('JR', 'Junior'),
#        ('SR', 'Senior'),
#        ]
#    call_name=models.CharField(max_length=200)
#    readable_name=models.CharField(max_length=200)
#    def custom_choice(call_name,readable_name):
#        sub_choices.append((call_name,readable_name))

#    entrys= models.ForeignKey(entry)
  
#    subject_text = models.CharField(max_length=200, choices=)
#    def __unicode__(self):
#        return self.subject_text
#import ipdb
#ipdb.set_trace()
