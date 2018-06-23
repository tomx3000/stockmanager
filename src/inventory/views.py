from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Item
# Create your views here.


def FBV(request,color=None,*args,**kagrs):
	# print(args)
	# print(kagrs)

	# method one
	# try :
	# 	obj = Item.objects.get(color=kagrs['color'])
	# except:
	# 	obj=Item.objects.all().first()

	# method 2
	# qs=Item.objects.filter(color=kagrs['color'])
	# if qs.exists() and qs.count()>=1:
	# 	obj=qs.first()
	
	# method 3
	obj=get_object_or_404(Item,id=color)
	obj_color=obj.item_name
	# print(request.method)
	
	return HttpResponse('hello FBV'+obj_color)


class MyView(View):
	def get(self,request,*args,**kagrs):
		return HttpResponse('hello CBV')


class HomePage(View):
	def get(self,request,*args,**kagrs):
		return render(request,'home/base.html',{})

class Inventory(View):
	def get(self,request,*args,**kargs):
		return render(request,'inventory/homepage.html',{})