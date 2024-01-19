from django.db import models
from django.utils.text import slugify

# Create your models here.
class NewsModel(models.Model):
    title = models.CharField(
        max_length=200,
        
    )
    content = models.TextField()
    category = models.CharField(
        max_length=50
    )
    published = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    slug = models.SlugField(
        blank=True,
        max_length=50,
        editable=False
    )

    def __str__(self):
        return f"{self.id}. {self.title}"
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()