from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment, Clap, Vote
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"


class PostCreateView(LoginRequiredMixin, CreateView):
    fields = ['title', 'content']
    model = Post
    template_name = "blog/new_post.html"
    success_url = "/"

    def form_valid(self, form):
        print(form)
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)
    