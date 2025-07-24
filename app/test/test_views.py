import pytest
from django.urls import reverse
@pytest.mark.django_db
def test_lista_empleados_view(client):
    response = client.get(reverse('lista_categorias'))
    assert response.status_code == 200
    assert "Lista de categorías" in response.content.decode()