from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post, Comment

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', { 'post': post })


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = '/posts/'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text']

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'

class CommentList(ListView):
  model = Comment

class CommentDetail(DetailView):
  model = Comment

class CommentCreate(CreateView):
  model = Comment
  fields = ['title', 'text']

class CommentUpdate(UpdateView):
  model = Comment
  fields = ['title', 'text']

class CommentDelete(DeleteView):
  model = Comment
  success_url = '/comments/'
