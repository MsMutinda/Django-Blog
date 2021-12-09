from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Category  # the . in models means current directory/application
from .forms import PostForm, EditForm
import random
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    categories = Category.objects.all()
    blogs = Post.objects.order_by('-created_date')[:4]
    featured_post = random.choice(Post.objects.all())

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({'categories': self.categories, 'blogs': self.blogs, 'featured_post': self.featured_post})
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # override form_valid() to add the blog author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


def category_filter(request, name):
    filtered_blogs = Post.objects.filter(category=name)
    # filtered_blogs = Post.objects.filter(category=name.replace('-', ' '))
    return render(request, 'category.html', {'name': name, 'filtered_blogs': filtered_blogs})


def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'user': user, 'user_posts': user_posts})
