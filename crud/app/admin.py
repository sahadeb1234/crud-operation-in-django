from django.contrib import admin
# from model import Student

# # Register your models here.
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display=('id', 'name', 'email', 'password')
from .models  import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
     list_display=('id', 'name', 'email', 'password')