from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import auth_user

admin.site.register(auth_user)

# Register your models here.
