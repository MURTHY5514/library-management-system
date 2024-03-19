from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    publication_date=models.DateField(auto_now_add=True)
    publisher=models.CharField(max_length=255)
    language=models.CharField(max_length=255)
    pages=models.PositiveIntegerField()
    summary=models.TextField()
    

    