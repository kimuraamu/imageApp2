from django.db import models

class Document(models.Model):
    photo = models.ImageField(upload_to='documents/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
