from django.contrib import admin

# Register your models here.
from .models import warehouseadapp

class warehousedbappAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at", "is_published", )
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
admin.site.register(warehouseadapp, warehousedbappAdmin)

