from django.db import models

# Create your models here.
class AddBook(models.Model):
    BookId = models.IntegerField()
    Title = models.CharField(max_length = 100)
    Author = models.CharField(max_length=50)   
    
class RBook(models.Model):
    BookId = models.IntegerField()
         
    