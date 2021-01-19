"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


#needed urls from the myblog application are imported into this file
urlpatterns = [
    path('admin/', admin.site.urls),  # for all urls starting with admin/
    path('', include('myblog.urls'))  # sets the default page 127.0.0.1 as our home page,
    # which then looks to (/is redirected to) myblog.urls for further instructions
]

