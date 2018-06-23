from rest_framework import routers
from inventory.viewsets import SalesViewSet,StoreViewSet,EmployeeViewSet,CompanyViewSet,CustomerViewSet,InventoryViewSet,ItemViewSet

router = routers.DefaultRouter()
router.register(r'sale', SalesViewSet)
router.register(r'store', StoreViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'item', ItemViewSet)