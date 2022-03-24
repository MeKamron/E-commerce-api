from django.urls import path, include
from orders.api.v1.urls import router as v1_router

urlpatterns = [path('v1/', include(v1_router.urls))]
