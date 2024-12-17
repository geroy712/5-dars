from django.db import models
from django.utils.timezone import now 
"""
Tepadagi now funksiyasi hozirgi vaqtni olish uchun ishlatildi. 
Nimaga agar Course ga Course ochilgan vaqtni qo`lda kiritilmasa avtomatik tarzda hozirgi vaqtni kiritish uchun ishlatilgan
""" 

class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    course_type = models.TextField(blank=True)
    teacher = models.TextField(blank=True)
    created_at = models.DateField(default=now, blank=True)
    student_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, null=True, blank=True)
    photo = models.ImageField(upload_to="post/photos/", null=True, blank=True)
    birth = models.DateField(null=True, blank=True)  
    enrolled_at = models.DateField(null=True, blank=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
