import pytest

from app.service.server import app


class TestServer:

    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_health_endpoint(self, client):
        response = client.get('/health')
        assert response.status_code == 200
        assert response.get_json()['message'] == "Running"
