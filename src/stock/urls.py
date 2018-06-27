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

from inventory.views import AcceptSale,MyView,HomePage,Inventory,AcceptSaleAll,DeclineSaleAll,Product,Counter,Settings,Login

urlpatterns = [
path('admin/', admin.site.urls),
# sales
path('sale/<slug:id>/', AcceptSale),
path('saledecline/', DeclineSaleAll),
path('saleaccept/', AcceptSaleAll),

# path('/sale/', MyView.as_view()),

# path('home/', HomePage.as_view(),name='base'),
path('order/', Inventory.as_view(),name='order'),

path('product/', Product,name='product'),
path('counter/', Counter,name='counter'),
path('settings/', Settings,name='settings'),

path('login/', Login,name='login'),




path('inventory/', include('inventory.urls')),
path('api/',include(router.urls)),

path('home/',TemplateView.as_view(template_name='home/base.html'),name='base'),

]
