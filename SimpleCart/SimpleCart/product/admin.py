from django.contrib import admin
from .models import ProductModel

class AdminFormat(admin.ModelAdmin):
    readonly_fields = [
        "created",
        "updated"
    ]

admin.site.register(ProductModel, AdminFormat)