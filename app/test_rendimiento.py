import time
import pytest
from django.urls import reverse
@pytest.mark.django_db
def test_homepage_latency(client):
    start = time.time()
    response = client.get(reverse('lista_productos'))
    duration = time.time() - start
    assert response.status_code == 200
    assert duration < 0.1 # menos de 100 ms
