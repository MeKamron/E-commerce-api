import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from shop.factories import CategoryFactory, UserFactory


@pytest.mark.django_db
def test_anonymous_regular_user(api_client):
    """
    Check if anonymous and regular users are allowed to list and retrieve
    but not create, update, delete
    :param api_client:
    :return:
    """
    response = api_client.get(reverse("category-list"))
    assert response.status_code == status.HTTP_200_OK

    category = CategoryFactory()
    response = api_client.get(reverse("category-detail", args=[category.id]))
    assert response.status_code == status.HTTP_200_OK

    response = api_client.post(reverse("category-list"))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.put(reverse("category-detail", args=[category.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client.delete(reverse("category-detail", args=[category.id]))
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
    response = api_client.post(reverse("category-list"), {"name": "test_category"})
    assert response.status_code == status.HTTP_201_CREATED

    category = CategoryFactory()
    response = api_client.put(reverse("category-detail", args=[category.id]), {"name": "test_category"})
    assert response.status_code == status.HTTP_200_OK

    response = api_client.delete(reverse("category-detail", args=[category.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT

