from django.db import models
from users.models import User

# Create your models here.
class AddBlog(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
