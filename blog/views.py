from django.views.generic import ListView, DetailView
from .models import Post

class Postlist(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post


