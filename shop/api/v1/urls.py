from .views import CategoryViewset, ProductViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"categories", CategoryViewset)
router.register(r"products", ProductViewset)
