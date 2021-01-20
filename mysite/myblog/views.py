from django.shortcuts import render, get_object_or_404
from .models import Post  # the . in models means current directory/application
# this will import the Post model code from models.py
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'myblog/post_list.html', {'posts': posts})  # render function with a request parameter,
    # and link to the template file. {} will hold things that may need to be added for the template to use


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # get_object_or_404 will handle cases where a non-existent post pk
    # is requested
    return render(request, 'myblog/post_detail.html', {'post': post})


