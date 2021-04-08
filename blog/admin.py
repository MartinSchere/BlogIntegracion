from django.contrib import admin
from .models import Post, Comment, Vote, Clap

admin.site.register([Post, Comment, Vote, Clap])