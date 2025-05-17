from django.shortcuts import render
from .models import BlogPost

def index(request):
    latest_posts = BlogPost.objects.order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})

def detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/detail.html', {'post': post})
