from django import template

from myblog.models import Category

register = template.Library()


@register.simple_tag
def blog_categories(request):
    categories = Category.objects.all()
    return categories
