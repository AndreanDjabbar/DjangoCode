from django.db import models

class ProductModel(models.Model):
    product_name = models.CharField(
        max_length=100
    )
    product_stock = models.PositiveIntegerField()
    product_description = models.CharField(
        max_length=300
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return f"{self.id}. {self.product_name}"