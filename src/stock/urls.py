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

from inventory.views import AcceptSale,MyView,HomePage,Inventory,AcceptSaleAll,DeclineSaleAll,ViewProduct,ViewCounter,ViewExpense,ViewSettings,ViewLogin,ViewCustomer,ViewOrder,ViewAuthorize,AuthorizeSale,IssueSale,ViewProfile,ChangeUsername,ChangePassword,increseItem,decreaseItem,increaseAccount,decreaseAccount,updateUpDownAccount,resetPassword

urlpatterns = [
path('admin/', admin.site.urls),

# sales
path('sale/<slug:id>/', AcceptSale),
path('username/<slug:id>/<slug:username>/', ChangeUsername),
path('userpass/<slug:id>/<slug:oldpassword>/<slug:firstnewpassword>/<slug:secondnewpassword>/<slug:username>/', ChangePassword),

# items
path('increaseitem/<slug:id>/<slug:quantity>/',increseItem ),
path('decreaseItem/<slug:id>/<slug:quantity>/',decreaseItem ),

# account
path('increaseaccount/<slug:id>/<slug:amount>/',increaseAccount ),
path('decreaseaccount/<slug:id>/<slug:amount>/',decreaseAccount ),
path('updownaccount/<slug:id>/<slug:amount>/',updateUpDownAccount ),

# user
path('resetpass/<slug:id>/', resetPassword),

# path('getallsales/', GetAllSale),
path('saledecline/', DeclineSaleAll),
path('saleaccept/', AcceptSaleAll),
path('authorizesale/<slug:id>/', AuthorizeSale),
path('issuesale/<slug:id>/', IssueSale),


# path('/sale/', MyView.as_view()),

# path('home/', HomePage.as_view(),name='base'),
path('order/', ViewOrder,name='order'),

path('product/', ViewProduct,name='product'),
path('counter/', ViewCounter,name='counter'),
path('expense/', ViewExpense,name='expense'),
path('customer/', ViewCustomer,name='customer'),
path('settings/', ViewSettings,name='settings'),
path('authorize/', ViewAuthorize,name='authorize'),
path('profile/', ViewProfile,name='profile'),
path('login/', ViewLogin,name='login'),




path('inventory/', include('inventory.urls')),
path('api/',include(router.urls)),

# path('home/',TemplateView.as_view(template_name='home/base.html'),name='base'),
path('',HomePage.as_view(),name='base'),


]
