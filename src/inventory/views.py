from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views import View


from .models import Sales,Store,Employee,Company,Customer,Inventory,Item
from .forms import ItemForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

@csrf_exempt
def AcceptSale(request,*args,**kargs):
	
	sale=Sales.objects.filter(id=kargs['id'])
	updatesale=sale.update(sales_received=True)
	item=Item.objects.filter(id=sale.first().item.id)
	item.update(item_size=item.first().item_size-sale.first().sales_quantity)

	print(kargs['id'])
	# print(request.POST)
	return HttpResponse('ok')

@csrf_exempt
def AcceptSaleAll(request,*args,**kargs):
	sales=Sales.objects.filter(sales_received=False)
	if sales.exists() and sales.count()>=1:
		for sale in sales:
			sale.sales_received=True
			sale.save()
			item=Item.objects.filter(id=sale.item.id)
			item.update(item_size=item.first().item_size-sale.sales_quantity)

	return HttpResponse('ok')

@csrf_exempt
def DeclineSaleAll(request,*args,**kargs):
	
	Sales.objects.filter(sales_received=False).delete()
	
	return HttpResponse('ok')

class MyView(View):
	def get(self,request,*args,**kagrs):
		return HttpResponse('hello CBV')

	def post(self,request,*args,**kagrs):
		print(request.POST['customer'])
		item=Item.objects.filter(id=request.POST['item'])
		customer=Customer.objects.filter(id=1)
		sale_order=Sales.objects.create(sales_quantity=request.POST['sales_quantity'],sales_amount=request.POST['sales_amount'],item=item,user=request.user,customer=customer)

		sale_order.save()
		return HttpResponse('ok')
class HomePage(View):
	def get(self,request,*args,**kagrs):

		return render(request,'home/base.html',{})

class Inventory(View):
	def get(self,request,*args,**kargs):
		form=ItemForm()

		return render(request,'inventory/homepage.html',{'form':form})


def Product(request,*args,**kargs):
	form=ItemForm()

	return render(request,'inventory/product.html',{'form':form})


def Counter(request,*args,**kargs):
	form=ItemForm()

	return render(request,'inventory/inventory.html',{'form':form})

def Settings(request,*args,**kargs):

	form=ItemForm()

	return render(request,'inventory/settings.html',{'form':form})

def Login(request,*args,**kargs):
	form=ItemForm()
	if(request.method=='POST'):

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:

		    # login(request, user)

		    # logout(request)
		    return redirect('base')

		else:
			return render(request,'inventory/login.html',{'form':form})	

	elif(request.method=='GET'):
		return render(request,'inventory/login.html',{'form':form})		

	

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
	# obj=get_object_or_404(Item,id=color)
	# obj_color=obj.item_name
	# # print(request.method)
	# sales=Sales.objects.filter(id=request.POST['id'])
	



		# sales=Sales.objects.filter(sales_received=False)
	# if sales.exists() and sales.count()>=1:	
	# 	for sale in sales:
	# 		sale.update(sales_received=True)
	# else:
	# 	sales.update(sales_received=True)

