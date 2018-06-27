from rest_framework import viewsets
from .models import Sales,Store,Employee,Company,Customer,Inventory,Item
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions

from .serializers import SalesSerializer,StoreSerializer,EmployeeSerializer,CompanySerializer,CustomerSerializer,InventorySerializer,ItemSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class SalesViewSet(viewsets.ModelViewSet):

	queryset=Sales.objects.all()
	serializer_class=SalesSerializer
	# permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
                          


	def list(self,request):
		# user=request.user.id
		# print(user)
		# qs = Sales.objects.filter(user=user)

		qs = Sales.objects.filter(id__gte=1)

		serializer=SalesSerializer(qs,many=True)

		return Response({'serial':serializer.data})

	# @csrf_exempt
	# def creaate(self,request):
	# 	print('posted')
	# 	item=Item.objects.filter(id=request.POST['item'])
	# 	customer=Customer.objects.filter(id=1)
	# 	sale_order=Sales.objects.create(sales_quantity=request.POST['sales_quantity'],sales_amount=request.POST['sales_amount'],item=item,user=request.user,customer=customer)

	# 	return Response('serial')
	# def perform_create(self,serializer):
	# 	serializer.save(user=self.request.user)


class StoreViewSet(viewsets.ModelViewSet):
	queryset=Store.objects.all()
	serializer_class=StoreSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
	queryset=Company.objects.all()
	serializer_class=CompanySerializer

class CustomerViewSet(viewsets.ModelViewSet):
	queryset=Customer.objects.all()
	serializer_class=CustomerSerializer

class InventoryViewSet(viewsets.ModelViewSet):
	queryset=Inventory.objects.all()
	serializer_class=InventorySerializer

class ItemViewSet(viewsets.ModelViewSet):

	queryset=Item.objects.all()
	serializer_class=ItemSerializer





