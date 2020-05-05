from django.db import models
from django.urls import reverse

# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.id})

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})
