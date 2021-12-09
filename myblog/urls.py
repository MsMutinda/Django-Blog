from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView
# from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryListView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('new-post', AddPostView.as_view(), name="add_post"),
    path('post/<int:pk>/edit', EditPostView.as_view(), name="edit_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('new-category', AddCategoryView.as_view(), name="add_category"),
    path('posts/<str:name>', views.category_filter, name="category_filter"),
    # path('categories/<int:pk>', CategoryListView.as_view(), name="category_filter"),
    path('profile', views.profile, name='profile')
]
