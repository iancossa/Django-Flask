from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Category, Post


# Create your views here.
from .models import Post
from .form import PostForm

#Home
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

#Post Detail
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    

