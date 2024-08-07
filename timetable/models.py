from django.db import models
from users.models import Student
from .choices import DAY_OF_THE_WEEK


class Slot(models.Model):
    """Model to create TimeTable"""
    title = models.CharField(max_length=100,blank=True, null=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    timeslot = models.TimeField(auto_now=False, auto_now_add=False,null=True)
    endslot= models.TimeField(auto_now=False, auto_now_add=False,null=True)
    day = models.CharField(choices=DAY_OF_THE_WEEK.choices,max_length=1)
    year = models.PositiveSmallIntegerField()
    week = models.PositiveSmallIntegerField()
    user=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Student')

    def __str__(self):
        
        return self.user.full_name


class UserColors(models.Model):
    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    color=models.CharField(max_length=255, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color
