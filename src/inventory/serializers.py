from rest_framework import serializers

from .models import Sales,Store,Employee,Company,Customer,Inventory,Item

class SalesSerializer(serializers.ModelSerializer):
	class Meta:
		model =Sales
		fields ="__all__"

class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Store
		fields= "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields="__all__"

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model= Company
		fields="__all__"

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields="__all__"

class InventorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Inventory
		fields="__all__"

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model= Item
		fields="__all__"






