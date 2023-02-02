from django.db import models
from test1.models import Post
class Comments(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')

    def __str__(self) -> str:
        return self.name 