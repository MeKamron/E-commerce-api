from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from orders.api.access_policy import OrderAccessPolicy
from .serializers import OrderSerializer
from orders.models import Order
from shop.models import Product


class OrderViewset(ModelViewSet):
    permission_classes = (OrderAccessPolicy, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Order.objects.filter(customer=self.request.user)
        else:
            return Order.objects.all()

    def perform_create(self, serializer):
        order = serializer.save(customer=self.request.user)
        product = Product.objects.get(pk=order.product.pk)
        product.available_units -= order.quantity
        product.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        product = Product.objects.get(pk=instance.product.pk)
        product.available_units += instance.quantity
        product.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=['get'], url_path="get-order-cost")
    def get_order_cost(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        cost = order.get_cost()
        return Response({"cost": cost})
