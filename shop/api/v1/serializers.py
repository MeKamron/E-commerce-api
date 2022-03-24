from rest_framework import serializers

from shop.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'unit_cost',
            'price',
            'available_units',
            'created',
            'updated',
        ]
