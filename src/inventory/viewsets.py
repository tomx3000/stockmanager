from rest_framework import viewsets
from .models import Sales,Store,Employee,Company,Customer,Inventory,Item
from .serializers import SalesSerializer,StoreSerializer,EmployeeSerializer,CompanySerializer,CustomerSerializer,InventorySerializer,ItemSerializer


class SalesViewSet(viewsets.ModelViewSet):
	queryset=Sales.objects.all()
	serializer_class=SalesSerializer

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


