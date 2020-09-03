from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    publishing_house = models.CharField(max_length=100)
    upvotes = models.IntegerField(default=0)
