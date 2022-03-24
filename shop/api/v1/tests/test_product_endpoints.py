import pytest
from shop.factories import UserFactory, ProductFactory, CategoryFactory
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_anonymous_user(api_client):
    """
    Check if anonymous and regular users are allowed to list and retrieve
    but not create, update, delete
    :param api_client:
    :return:
    """
    response = api_client.get(reverse("product-list"))
    assert response.status_code == status.HTTP_200_OK

    product = ProductFactory()
    response = api_client.get(reverse("product-detail", args=[product.id]))
    assert response.status_code == status.HTTP_200_OK

    response = api_client.post(reverse("product-list"))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.put(reverse("product-detail", args=[product.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.delete(reverse("product-detail", args=[product.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_admin_user(api_client):
    """
    Check if staff user is allowed to perform CRUD
    :param api_client:
    :return:
    """
    user = UserFactory(is_staff=True)
    api_client.force_authenticate(user)

    category = CategoryFactory()
    data = dict(
        name="Laptop",
        category=category.id,
        unit_cost=10.0,
        price=15.0,
        available_units=50
    )
    response = api_client.post(reverse("product-list"), data)
    assert response.status_code == status.HTTP_201_CREATED

    product = ProductFactory()
    response = api_client.put(reverse("product-detail", args=[product.id]), data)
    assert response.status_code == status.HTTP_200_OK

    response = api_client.delete(reverse("product-detail", args=[product.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
