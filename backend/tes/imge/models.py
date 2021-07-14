from django.db import models

# Create your models here.

class Image(models.Model):
    img = models.ImageField()
    
    def __str__(self):
        return self.id + self.img