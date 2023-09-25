from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.email}"

# create table user(name varchar(100))
