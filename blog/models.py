from django.db import models

# Create your models here.

class Blog(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='portfolio/images/')


def __str__(self):
    return self.title
