from django.contrib import admin

# Register your models here.
from .models import Users, Items

admin.site.register(Users)
admin.site.register(Items)
