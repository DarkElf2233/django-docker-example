from django.contrib import admin
from django.contrib.auth.models import Group
from myapp.models import Book

admin.site.unregister(Group)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
