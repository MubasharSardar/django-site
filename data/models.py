from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class pydata(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(config_name='special')
    date = models.DateField()


    def __str__(self):
        return self.title