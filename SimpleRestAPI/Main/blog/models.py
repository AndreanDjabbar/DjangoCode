from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

class DataModel(models.Model):
    name = models.CharField(
        max_length=100
    )
    age = models.PositiveIntegerField()
    gender_choice = (
        ('F', "Female"),
        ('M', "Male"),
        ('N', "None")
    )
    gender = models.CharField(
        max_length=1,
        choices=gender_choice,
        default=gender_choice[2]
    )
    id_card_format = RegexValidator(
        regex=r"^[0-9]*$",
        message="Id Card Number must be integer type"
    )
    id_card_number = models.CharField(
        max_length=10,
        validators=[id_card_format]
    )
    address = models.CharField(
        max_length=200
    )
    is_married = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    slug = models.SlugField(
        blank=True
    )

    def __str__(self):
        return f"{self.id}. {self.name}"
    
    def save(self, *args, **kwargs):
        kwargs["force_insert"] = True
        self.slug = slugify(self.name)
        super().save()