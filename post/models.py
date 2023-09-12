from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to the current time when created
    
    image_one = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images/')
    image_three = models.ImageField(upload_to='images/')

