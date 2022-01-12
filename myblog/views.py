from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Post, Category  # the . in models means current directory/application
from .forms import PostForm, EditForm, EditCategoryForm
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


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # override form_valid() to add the blog author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.total_likes()
        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


def LikePost(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


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


class CategoriesView(ListView):
    model = Category
    template_name = 'categories_list.html'


def category_filter(request, name):
    filtered_blogs = Post.objects.filter(category=name)
    # filtered_blogs = Post.objects.filter(category=name.replace('-', ' '))
    return render(request, 'category.html', {'name': name, 'filtered_blogs': filtered_blogs})


class CategoryEdit(UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'category_edit.html'
    success_url = reverse_lazy('categories_list')


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('categories_list')


def profile(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'user_posts': user_posts})
