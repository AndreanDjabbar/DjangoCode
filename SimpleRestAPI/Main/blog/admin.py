from django.contrib import admin
from .models import DataModel

class FormatAdmin(admin.ModelAdmin):
    readonly_fields = [
        "created",
        "updated",
        "slug"
    ]

admin.site.register(DataModel, FormatAdmin)