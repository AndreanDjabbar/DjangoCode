from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "product_name",
            "product_stock",
            "product_description"
        ]
        widgets = {
            "product_name":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Product Name"
                }
            ),
            "product_stock":forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "product_description":forms.Textarea(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Product Description"
                }
            )
        }