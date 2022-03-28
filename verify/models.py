from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=158)
    pwd = models.CharField(max_length=155)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

