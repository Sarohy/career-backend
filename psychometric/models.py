from django.db import models
from users.models import Student
from ckeditor.fields import RichTextField

# Create your models here.

class TestType(models.Model):
    type=models.CharField(max_length=300)
    description= RichTextField(null=True, blank=True)

    def __str__(self):
        return self.type

class PsychometricTest(models.Model):
    name = models.CharField(max_length=300)
    intro=models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(PsychometricTest, related_name="question",on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    type=models.ForeignKey(TestType,on_delete=models.CASCADE)
    def __str__(self):
        return self.question

class Answer(models.Model):
    question= models.ForeignKey(Question,related_name="answer",on_delete=models.CASCADE)
    answer=models.CharField(max_length=1000)
    weightage=models.IntegerField()
    def __str__(self):
        return self.answer

class TestResult(models.Model):
    user=models.ForeignKey(Student, blank=True, null=True,on_delete=models.CASCADE)
    test=models.ForeignKey(PsychometricTest,blank=True, null=True, on_delete=models.CASCADE)
    score=models.IntegerField(null=True)
    def __str__(self):
        return self.user.full_name
    
class TestResultDetail(models.Model):
    result=models.ForeignKey(TestResult, on_delete=models.CASCADE)
    question=models.ForeignKey(Question,related_name="result", on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,related_name="result", on_delete=models.CASCADE)
   

class CareerIdea(models.Model):
    type = models.OneToOneField(TestType, on_delete=models.CASCADE)
    idea = RichTextField(null=True, blank=True)


class ChoiceIdea(models.Model):
    type = models.OneToOneField(TestType, on_delete=models.CASCADE)
    idea = RichTextField(null=True, blank=True)


class StudyTips(models.Model):
    type = models.ForeignKey(TestType, on_delete=models.CASCADE)
    # title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
