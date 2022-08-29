from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass