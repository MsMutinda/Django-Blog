from django.shortcuts import render
from .models import Post  # the . in models means current directory/application
# this will import the Post model code from models.py
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'myblog/post_list.html', {'posts': posts})  # render function with a request parameter,
    # and link to the template file. {} will hold things that may need to be added for the template to use


