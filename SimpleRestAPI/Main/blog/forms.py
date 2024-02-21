from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import DataModel
from django.core.validators import RegexValidator

class DataForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = [
            "name",
            "age",
            "gender",
            "id_card_number",
            "address",
            "is_married"
        ]
        widgets = {
            "name":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Name"
                }
            ),
            "age":forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Age"
                }
            ),
            "gender":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),
            "id_card_number":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Id Card Number"
                }
            ),
            "address":forms.Textarea(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Address"
                }
            ),
            "is_married":forms.CheckboxInput(
                attrs={
                    "class":"form-check-input"
                }
            )
        }