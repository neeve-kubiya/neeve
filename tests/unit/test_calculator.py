import pytest
from src.core.calculator import FinancialCalculator

class TestFinancialCalculator:
    def setup_method(self):
        self.calculator = FinancialCalculator()
        
    def test_compound_interest_calculation(self):
        # Test with simple values
        result = self.calculator.calculate_compound_interest(
            principal=1000,
            rate=0.05,
            time=2,
            compounds_per_year=12
        )
        # This will fail due to the intentional bug in the formula
        assert round(result, 2) == 1104.94
        
    def test_invalid_input_types(self):
        with pytest.raises(TypeError):
            self.calculator.calculate_compound_interest(
                principal="1000",  # Invalid type
                rate=0.05,
                time=2,
                compounds_per_year=12
            )
            
    def test_operation_recording(self):
        self.calculator.calculate_compound_interest(1000, 0.05, 2, 12)
        history = self.calculator._history
        
        assert len(history) == 1
        assert history[0]["operation"] == "COMPOUND_INTEREST"
        assert history[0]["inputs"]["principal"] == 1000 