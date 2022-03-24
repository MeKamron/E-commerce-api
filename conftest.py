import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """A Django REST Framework api tests client instance."""
    return APIClient()
