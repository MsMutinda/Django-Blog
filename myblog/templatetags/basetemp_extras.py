from django import template

from myblog.models import Category

register = template.Library()


@register.simple_tag
def blog_categories(request):
    categories_list = Category.objects.all().values_list('name')
    categories = []
    for cat in categories_list:
        categories.append(cat)
    return categories
