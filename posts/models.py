from django.db import models

# Create your models here.

# Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=240)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title[0:25]