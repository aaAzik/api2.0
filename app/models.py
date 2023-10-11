from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    title = models.CharField(max_length=230)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)
    available = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

