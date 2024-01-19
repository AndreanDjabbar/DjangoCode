from django import forms
from .models import NewsModel

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = [
            "title",
            "content",
            "category"
        ]
        widgets = {
            "title":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Title"
                }
            ),
            "content":forms.Textarea(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Content"
                }
            ),
            "category":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Category"
                }
            )
        }