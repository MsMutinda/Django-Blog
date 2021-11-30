from django.urls import path
from .views import PostDetailView, AddPostView, EditPostView, DeletePostView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('new-post', AddPostView.as_view(), name="add_post"),
    path('post/<int:pk>/edit', EditPostView.as_view(), name="edit_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout')
]
