from django.db import models
from django.utils.text import slugify

class Maqola(models.Model):
    title = models.CharField(max_length=50)
    sana = models.DateField()
    text = models.TextField()
    photo = models.FileField()
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
