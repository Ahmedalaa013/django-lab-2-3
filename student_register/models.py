from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    st_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=12)

