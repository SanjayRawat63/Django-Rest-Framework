from django.contrib import admin
from pkg_resources import empty_provider

from emplist_app.models import employees

# Register your models here.
admin.site.register(employees)