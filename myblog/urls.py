from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, \
    CategoriesView, category_filter, CategoryEdit, CategoryDelete, profile


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('new-post', AddPostView.as_view(), name="add_post"),
    path('post/<int:pk>/edit', EditPostView.as_view(), name="edit_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('all-categories', CategoriesView.as_view(), name="categories_list"),
    path('new-category', AddCategoryView.as_view(), name="add_category"),
    path('posts/<str:name>', category_filter, name="category_filter"),
    # path('categories/<int:pk>', CategoryListView.as_view(), name="category_filter"),
    path('category/<int:pk>/edit', CategoryEdit.as_view(), name="category_edit"),
    path('category/<int:pk>/delete', CategoryDelete.as_view(), name="category_delete"),
    path('profile', profile, name='profile')
]
