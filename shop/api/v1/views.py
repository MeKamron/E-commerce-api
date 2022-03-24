from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from shop.models import Category, Product
from shop.api.access_policy import CategoryProductAccessPolicy
from .serializers import CategorySerializer, ProductSerializer
from shop.services import clean_date


class CategoryViewset(ModelViewSet):
    permission_classes = (CategoryProductAccessPolicy,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(ModelViewSet):
    permission_classes = (CategoryProductAccessPolicy,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'], url_path='get-summary/(?P<date>[^/.]+)')
    def get_summary(self, *args, **kwargs):
        """
        Return summary information about a product based on a date
        :param args:
        :param kwargs:
        :return:
        """
        date = kwargs.get('date')
        date = clean_date(date)
        product = self.get_object()
        date_based_orders = product.orders.filter(records__history_type='+').filter(records__history_date__date=date)
        income = sum([order.get_cost() for order in date_based_orders])
        profit = sum([order.get_profit() for order in date_based_orders])
        units_sold = sum([order.quantity for order in date_based_orders])
        orders_count = date_based_orders.count()
        return Response({"income": income, "profit": profit, "units_sold": units_sold, "orders_count": orders_count})
