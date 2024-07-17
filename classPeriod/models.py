from django.db import models
from course.models import Course



# Create your models here.

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #  class= models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=50)