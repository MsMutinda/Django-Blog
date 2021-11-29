from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Post  # the . in models means current directory/application
import random
from django.views.generic import ListView, DetailView


def home(request):
    blogs = list(Post.objects.all())
    featured_post = random.choice(blogs)
    return render(request, 'myblog/home.html', {'blogs': blogs, 'featured_post': featured_post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/post_details.html'


@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'myblog/profile.html', {'user_posts': user_posts})


@login_required
def logout(request):
    logout(request)
    return render(redirect('%s?next=%s' % (settings.LOGIN_URL, request.path)))

