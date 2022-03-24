from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
        blank=True
    )
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    history = HistoricalRecords(related_name='records')

    def __str__(self):
        return f'Order on {self.product.name} by {self.customer.username}'

    def get_cost(self):
        return self.product.price * self.quantity

    def get_profit(self):
        return (self.product.price - self.product.unit_cost) * self.quantity
