from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.first_name + ' ' + self.last_name