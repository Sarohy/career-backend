from django.db import models
from users.models import Student
from ckeditor.fields import RichTextField

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=700, null=True, default='')
    image = models.ImageField(upload_to='Quiz_images',null=True,blank=True)
    youtube_title = models.CharField(max_length=300,null=True,blank=True)
    youtube_link= models.CharField(max_length=700, null=True, blank=True, default='')
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'education'

    
class Question(models.Model):
    quiz=models.ForeignKey(Quiz,related_name="question", on_delete=models.CASCADE)
    question = RichTextField()
    
    def __str__(self):
        return self.question
    
    class Meta:
        app_label = 'education'

class Answer(models.Model):
    question= models.ForeignKey(Question,related_name="answer",on_delete=models.CASCADE)
    answer=models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer

class QuizResult(models.Model):
    user=models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE, default='1')
    score=models.IntegerField()


    def __str__(self):
        return self.user.full_name

class QuizResultDetail(models.Model):
    result= models.ForeignKey(QuizResult, on_delete=models.CASCADE)
    question= models.ForeignKey(Question,related_name="result",on_delete=models.CASCADE)
    answer= models.ForeignKey(Answer,related_name="result",on_delete=models.CASCADE)

    def __str__(self):
        return self.result.user.full_name


class QuizLimit(models.Model):
    limit = models.IntegerField()
