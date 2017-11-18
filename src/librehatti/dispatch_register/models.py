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



class entry(models.Model):
    """
    Handling dispatch register
    """
    pub_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    agency = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)


