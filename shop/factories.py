import factory
from factory import fuzzy
from django.contrib.auth import get_user_model
from .models import Category, Product

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: x.email)
    email = factory.Sequence(lambda x: f'test.user.{x}@test.com')
    first_name = factory.Sequence(lambda x: f'first_name.test.{x}')
    last_name = factory.Sequence(lambda x: f'last_name.test.{x}')

    @classmethod
    def create_admin(cls):
        """
        Create admin user
        :return:
        """
        return cls(is_staff=True)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    unit_cost = factory.fuzzy.FuzzyDecimal(low=0.0)
    price = factory.fuzzy.FuzzyDecimal(low=0.0)
    available_units = factory.fuzzy.FuzzyInteger(low=1)
