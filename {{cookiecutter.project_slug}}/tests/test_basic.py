from django.urls import reverse


def test_frontpage(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'Index page' in str(response.body)
