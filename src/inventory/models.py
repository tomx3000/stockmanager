from django.db import models
from django.conf import settings
from .utility import generate_manufucture
# Create your models here.

SOMEFIXED = getattr(settings,'FIXE_VALUE',3)

class ItemManager(models.Manager):
	# def all(self,*args,**kargs):
	# 	query_set=super(ItemManager,self).all(*args,**kargs)
	# 	qs=query_set.filter(item_color="black")

	# 	return qs

	def check_amount(self,itmes=None):
		qs=Item.objects.filter(id__gte=1)
		amount=0

		# if itmes is not None and isinstance(items,int):
		# 	qs = qs.oder_by('-id')[:items]

		for row in qs:
			amount+=row.item_price
		return "Total :{a}".format(a=amount)	


class Company(models.Model):
	company_name=models.CharField(max_length=40,)
	company_address=models.CharField(max_length=40,)
	company_phone=models.CharField(max_length=20,)
	company_email=models.EmailField(max_length=40,)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)


	def __str__(self):
		return str(self.company_name)
	pass

class Store(models.Model):
	company=models.ForeignKey(Company,on_delete=models.CASCADE)
	store_name=models.CharField(max_length=40,)
	store_address=models.CharField(max_length=40,)
	store_phone=models.CharField(max_length=20,)
	store_email=models.EmailField(max_length=40,)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)


	def __str__(self):
		return str(self.store_name)
	pass



class Customer(models.Model):
	customer_name=models.CharField(max_length=20,null=True,blank=True)
	customer_location=models.CharField(max_length=30,null=True,blank=True)
	customer_status=models.BooleanField(default=True)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return str(self.customer_name)


	pass
class Employee(models.Model):
	company=models.ForeignKey(Company,on_delete=models.CASCADE)
	employee_firstname=models.CharField(max_length=20)
	employee_secondname=models.CharField(max_length=20,null=True,blank=True)
	employee_thirdname=models.CharField(max_length=20,null=True,blank=True)
	employee_phone=models.CharField(max_length=20)
	employee_email=models.EmailField(null=True,blank=True)
	employee_position=models.CharField(max_length=20)
	employee_address=models.CharField(max_length=30)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return str(self.employee_firstname)
	pass


class Item(models.Model):
	store=models.ForeignKey(Store,on_delete=models.CASCADE)
	item_name=models.CharField(max_length=40,)
	item_price=models.FloatField( null=True,default=0.0)
	item_size=models.FloatField(null=True,blank=True)
	item_color=models.CharField(max_length=40,null=True,blank=True)
	item_manufucture=models.CharField(max_length=50,null=True,blank=True)
	item_expiration_date=models.DateField(null=True,blank=True)
	item_image=models.ImageField(null=True,blank=True)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

	objects=ItemManager()
	items=ItemManager()

	def __str__(self):
		return str(self.item_name)+" "+str(self.item_color)


	def save(self,*args,**kargs):
		print('save')
		if self.item_manufucture is None or '':
			self.item_manufucture=generate_manufucture()
		
		super(Item,self).save(*args,**kargs)



class Inventory(models.Model):
	# userid
	item=models.ForeignKey(Item,on_delete=models.CASCADE)
	quantity=models.FloatField()
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)


	def __str__(self):
		return str(self.quantity)
	pass


class Sales(models.Model):
	item=models.ForeignKey(Item,on_delete=models.CASCADE)
	# userid
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
	sales_amount=models.FloatField()
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)


	def __str__(self):
		return str(self.item.item_name)+" :"+str(self.sales_amount)

	pass


	


# class Meta:
# 	odering = '-id'