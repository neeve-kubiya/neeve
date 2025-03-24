import pytest
from src.services.calculation_service import CalculationService
from src.core.exceptions import ValidationError

class TestCalculationService:
    def setup_method(self):
        self.service = CalculationService()
        
    def test_process_valid_investment_calculation(self):
        data = {
            "principal": 1000,
            "interest_rate": 0.05,
            "time_period": 2,
            "compounds_per_year": 12
        }
        
        result = self.service.process_investment_calculation(data)
        assert result["status"] == "success"
        assert "result" in result
        
    def test_missing_required_fields(self):
        data = {
            "principal": 1000,
            # Missing interest_rate
            "time_period": 2
        }
        
        with pytest.raises(ValidationError) as exc_info:
            self.service.process_investment_calculation(data)
        assert "Missing required field" in str(exc_info.value)
        
    # This test will fail due to missing validation
    def test_negative_values(self):
        data = {
            "principal": -1000,  # Negative principal
            "interest_rate": 0.05,
            "time_period": 2
        }
        
        with pytest.raises(ValidationError) as exc_info:
            self.service.process_investment_calculation(data)
        assert "Negative values not allowed" in str(exc_info.value) 