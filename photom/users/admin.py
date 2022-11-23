from django.contrib import admin, auth
from django.contrib.auth import models
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AnonymousUser

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


