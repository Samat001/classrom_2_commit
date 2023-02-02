from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title