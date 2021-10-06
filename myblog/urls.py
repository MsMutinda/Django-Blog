from django.urls import path  # imports django's function path
from . import views  # imports all views from the myblog application


urlpatterns = [
    path('', views.homepage, name='home'),
    path('profile', views.profile, name='profile'),
    path('blogs', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]
