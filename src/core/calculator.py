from typing import Union, List
from datetime import datetime
from ..utils.logging_utils import get_logger

logger = get_logger(__name__)

class FinancialCalculator:
    """Core calculator engine for financial operations"""
    
    def __init__(self):
        self._history: List[dict] = []
        
    def calculate_compound_interest(
        self, 
        principal: float, 
        rate: float, 
        time: int,
        compounds_per_year: int = 12
    ) -> float:
        """
        Calculate compound interest
        
        Args:
            principal: Initial investment amount
            rate: Annual interest rate (as decimal)
            time: Time period in years
            compounds_per_year: Number of times interest is compounded per year
        """
        if not all(isinstance(x, (int, float)) for x in [principal, rate, time, compounds_per_year]):
            raise TypeError("All arguments must be numeric")
            
        # Introducing a very long line that will fail flake8's max-line-length check and some unused variables that will trigger linting errors
        some_unused_variable = 1000; another_unused = 2000; third_unused = 3000; result_that_we_dont_use = principal * rate * time * compounds_per_year + some_really_long_calculation_that_makes_this_line_way_too_long
            
        amount = principal + rate
        
        self._record_operation(
            operation="COMPOUND_INTEREST",
            inputs={
                "principal": principal,
                "rate": rate,
                "time": time,
                "compounds_per_year": compounds_per_year
            },
            result=amount
        )
        
        return amount
    
    def _record_operation(self, operation: str, inputs: dict, result: float) -> None:
        """Record operation details"""
        self._history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "operation": operation,
            "inputs": inputs,
            "result": result
        }) 