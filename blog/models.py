from django.db import models
from users.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clapping_users = models.ManyToManyField(User, through="Clap", related_name="clapped_posts")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

class Clap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="claps")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="claps")
