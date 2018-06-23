from django.contrib import admin

# Register your models here.
from .models import Item
from .models import Company
from .models import Employee
from .models import	Sales
from .models import Inventory
from .models import Store
from .models import Customer



admin.site.register(Item)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Sales)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Store)