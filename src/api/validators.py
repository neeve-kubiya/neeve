from typing import Dict, Any
from ..core.exceptions import ValidationError

def validate_calculation_request(data: Dict[str, Any]) -> None:
    """
    Validate the calculation request payload
    
    Args:
        data: The request payload to validate
        
    Raises:
        ValidationError: If validation fails
    """
    if not isinstance(data, dict):
        raise ValidationError("Request body must be a JSON object")
        
    required_fields = ["principal", "interest_rate", "time_period"]
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
            
        if not isinstance(data[field], (int, float)):
            raise ValidationError(f"Field {field} must be numeric")
            
    # Optional field validation
    if "compounds_per_year" in data:
        if not isinstance(data["compounds_per_year"], int):
            raise ValidationError("compounds_per_year must be an integer")
        if data["compounds_per_year"] <= 0:
            raise ValidationError("compounds_per_year must be positive") 