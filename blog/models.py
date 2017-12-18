from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

class Tag(models.Model):
    name = models.CharField(max_length=64)
class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=256,blank=True)

    #关系
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title