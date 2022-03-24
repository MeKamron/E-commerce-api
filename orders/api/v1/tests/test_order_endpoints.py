import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from orders.factories import OrderFactory
from shop.factories import UserFactory, ProductFactory


@pytest.mark.django_db
def test_anonymous_user(api_client):
    """
    Check if anonymous users are not allowed to perform CRUD
    :param api_client:
    :return:
    """
    response = api_client.get(reverse("order-list"))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    order = OrderFactory()
    response = api_client.get(reverse("order-detail", args=[order.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.post(reverse("order-list"))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.put(reverse("order-detail", args=[order.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.delete(reverse("order-detail", args=[order.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_regular_user(api_client):
    """
    Check if regular users are allowed to perform CRUD
    :param api_client:
    :return:
    """

    user = UserFactory()
    api_client.force_authenticate(user)
    response = api_client.get(reverse("order-list"))
    assert response.status_code == status.HTTP_200_OK

    product = ProductFactory()
    order = OrderFactory(customer=user, product=product)
    response = api_client.get(reverse("order-detail", args=[order.id]))
    assert response.status_code == status.HTTP_200_OK

    response = api_client.post(reverse("order-list"), {"customer": user.id, "product": product.id})
    assert response.status_code == status.HTTP_201_CREATED

    response = api_client.put(reverse("order-detail", args=[order.id]))
    assert response.status_code == status.HTTP_200_OK

    response = api_client.delete(reverse("order-detail", args=[order.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
