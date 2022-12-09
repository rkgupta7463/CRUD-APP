from django.db import models

# Create your models here.
class StudentDB(models.Model):
    sname=models.CharField(max_length=50)
    semail=models.EmailField(max_length=30)
    phone=models.BigIntegerField()
    Branch=models.CharField(max_length=50)
    college=models.CharField(max_length=100)

    def __str__(self):
        return self.sname