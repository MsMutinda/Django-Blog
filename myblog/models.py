from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# self represents an instance of our class.
# By using it ware able to access the class methods and attributes

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()  # for long texts without any character limit
    likes = models.ManyToManyField(User, related_name='blog_posts')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + ' - by ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
