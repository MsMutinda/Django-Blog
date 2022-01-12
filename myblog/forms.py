from django import forms
from .models import Post, Category
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget


categories = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'text')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}, choices=categories),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(attrs={'summernote': {'width': '100%'}})
            # 'text': SummernoteTextField()
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'text')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}, choices=categories),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(attrs={'summernote': {'width': '100%'}})
            # 'text': SummernoteTextField()
        }


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
