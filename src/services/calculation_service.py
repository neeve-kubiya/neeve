from typing import Dict, Any, List
from ..core.calculator import FinancialCalculator
from ..core.exceptions import ValidationError
from ..utils.logging_utils import get_logger

logger = get_logger(__name__)

class CalculationService:
    """Service layer for handling financial calculations"""
    
    def __init__(self):
        self._calculator = FinancialCalculator()
        
    def process_investment_calculation(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process investment calculation request
        
        Args:
            data: Dictionary containing calculation parameters
        """
        try:
            self._validate_investment_data(data)
            
            result = self._calculator.calculate_compound_interest(
                principal=data["principal"],
                rate=data["interest_rate"],
                time=data["time_period"],
                compounds_per_year=data.get("compounds_per_year", 12)
            )
            
            return {
                "status": "success",
                "result": result,
                "metadata": {
                    "calculation_type": "compound_interest",
                    "parameters": data
                }
            }
            
        except ValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Calculation error: {str(e)}")
            raise
            
    def _validate_investment_data(self, data: Dict[str, Any]) -> None:
        """Validate investment calculation input data"""
        required_fields = ["principal", "interest_rate", "time_period"]
        
        # Intentional bug: Missing validation for negative values
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"Missing required field: {field}") 