from django.contrib import admin
from .models import padi
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(padi)
admin.site.unregister(Group)