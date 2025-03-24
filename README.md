# Financial Calculator Service

A microservice for handling financial calculations with proper separation of concerns, configuration management, logging, and API endpoints.

## Project Structure
```
src/
  ├── api/         # API routes and validators
  ├── core/        # Core business logic
  ├── services/    # Service layer
  └── utils/       # Utility functions
tests/
  ├── unit/        # Unit tests
  └── integration/ # Integration tests
```

## Setup and Running

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Run tests:
```bash
./build.sh
```

## API Endpoints

### POST /api/v1/calculate/investment
Calculate compound interest for an investment.

Request body:
```json
{
    "principal": 1000,
    "interest_rate": 0.05,
    "time_period": 2,
    "compounds_per_year": 12
}
```

Response:
```json
{
    "status": "success",
    "result": 1104.94,
    "metadata": {
        "calculation_type": "compound_interest",
        "parameters": {
            "principal": 1000,
            "interest_rate": 0.05,
            "time_period": 2,
            "compounds_per_year": 12
        }
    }
}
```

## Known Issues
This project contains intentional bugs for demonstration purposes:
1. Incorrect compound interest calculation formula
2. Missing validation for negative values
3. Incorrect logging configuration
4. Hard-coded configuration in app.py

## Testing
The project includes both unit and integration tests. The build will fail intentionally due to:
- Type checking errors
- Test failures from incorrect calculations
- Missing validations
- Coverage below 90% threshold 