from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True, max_length=100)
    marks = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


        
