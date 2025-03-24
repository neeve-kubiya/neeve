import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

class TestInvestmentAPI:
    def test_successful_calculation(self, client):
        data = {
            "principal": 1000,
            "interest_rate": 0.05,
            "time_period": 2,
            "compounds_per_year": 12
        }
        
        response = client.post(
            '/api/v1/calculate/investment',
            data=json.dumps(data),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result["status"] == "success"
        assert "result" in result
        
    def test_invalid_input(self, client):
        data = {
            "principal": "invalid",
            "interest_rate": 0.05,
            "time_period": 2
        }
        
        response = client.post(
            '/api/v1/calculate/investment',
            data=json.dumps(data),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        
    def test_missing_data(self, client):
        response = client.post(
            '/api/v1/calculate/investment',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400 