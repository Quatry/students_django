from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=30)

class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='marks')
    value = models.IntegerField(default=None)

