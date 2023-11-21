from django.contrib import admin
from Shop.models import *

# Register your models here.
admin.site.register([Vendor, Category, ApplicationArea, Product])
