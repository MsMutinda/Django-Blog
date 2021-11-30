from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .models import Post, Category  # the . in models means current directory/application
from .forms import PostForm, EditForm
import random
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    categories = Category.objects.all()
    blogs = list(Post.objects.order_by('-created_date')[:4])
    featured_post = random.choice(blogs)
    return render(request, 'myblog/home.html',
                  {'categories': categories, 'blogs': blogs, 'featured_post': featured_post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/post_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'
    # fields = '__all__'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'myblog/edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'myblog/delete_post.html'
    success_url = reverse_lazy('home')


@login_required
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'myblog/profile.html', {'user': user, 'user_posts': user_posts})


@login_required
def logout(request):
    logout(request)
    return render(redirect('%s?next=%s' % (settings.LOGIN_URL, request.path)))

