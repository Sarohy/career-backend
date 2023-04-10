from .validators import validate_file_size
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class School(models.Model):
    """Model to create School"""
    school = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    def __str__(self):
        return self.school

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=32, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Student(models.Model):
    """Model to create Student"""
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    school =  models.ForeignKey(School,on_delete=models.CASCADE,blank=True)
    profile_image = models.ImageField(upload_to='profile_images',null=True,blank=True,validators=[validate_file_size])  
    dob = models.DateField(null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
    city = models.CharField(max_length=50, blank=True,null=True)
    country = models.CharField(max_length=50, blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    eircode=models.CharField(max_length=7,null=True,blank=True)
    def __str__(self):
        """return name of Student"""
        return self.full_name
 

