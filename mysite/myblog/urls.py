from django.urls import path  # imports django's function path
from . import views  # imports all views from the myblog application


urlpatterns = [
    path('', views.post_list, name='post_list'),  # assigns a view called post_list to the root URL
    # anyone visiting the homepage will be taken here (views.post_list)
]
