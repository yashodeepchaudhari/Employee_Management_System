from django.db import models

# Create your models here.
class ADD_EMP(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    empid=models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    
    dept=models.CharField(max_length=15)

    def __str__(self):
        return self.name