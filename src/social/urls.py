from django.conf.urls import url
from django.urls import  path,include

from .views import socialSample
urlpatterns = [
path('app',socialSample,name='socialapp')
]