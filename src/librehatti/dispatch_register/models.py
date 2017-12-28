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

class remark_choices(models.Model):
    readable_name=models.CharField(max_length=200)
   
    def __str__(self):
        return self.readable_name

class sub_choices(models.Model):
    readable_name=models.CharField(max_length=200)
    def __str__(self):
        return self.readable_name

class entry(models.Model):
    """
    Handling dispatch register
    """
    dispatch_no = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    name_of_Dept_or_Client = models.ForeignKey(User)
    agency = models.CharField(max_length=200, blank=True)
    subject = models.ManyToManyField(sub_choices)
    remarks = models.ManyToManyField(remark_choices)
