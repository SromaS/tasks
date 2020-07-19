from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book admin interface"""
    list_display = ("id", "title", "author", "description")
    list_display_links = ("title",)
    readonly_fields = ("id",)
