from rest_framework.routers import SimpleRouter
from .views import OrderViewset

router = SimpleRouter()
router.register(r"orders", OrderViewset, basename="order")
