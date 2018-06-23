"""stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import  path,include
from .routers import router
from django.views.generic import TemplateView

from inventory.views import FBV,MyView,HomePage,Inventory

urlpatterns = [
path('admin/', admin.site.urls),
path('fbv/', FBV),
path('fbv/<slug:color>', FBV),
path('cbv/', MyView.as_view()),

# path('home/', HomePage.as_view(),name='base'),
path('test/', Inventory.as_view(),name='order'),
path('inventory/', include('inventory.urls')),
path('api/',include(router.urls)),

path('home/',TemplateView.as_view(template_name='home/base.html'),name='base'),

]
