from flask import Blueprint, request, jsonify
from ..services.calculation_service import CalculationService
from ..core.exceptions import ValidationError
from ..utils.logging_utils import get_logger

api = Blueprint('api', __name__)
logger = get_logger(__name__)

calculation_service = CalculationService()

@api.route('/calculate/investment', methods=['POST'])
def calculate_investment():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        result = calculation_service.process_investment_calculation(data)
        return jsonify(result), 200
        
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500 