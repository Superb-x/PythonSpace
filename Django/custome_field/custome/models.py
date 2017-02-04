from django.db import models
from .fields import CompressedTextField, ListField
# Create your models here.

class Article(models.Model):
    labels = ListField()
    content = CompressedTextField(null=True, default='')