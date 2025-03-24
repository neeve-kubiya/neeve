#!/bin/bash
set -e  # Exit on first error

echo "Setting up Python environment..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Running code formatting check..."
black --check .

echo "Running type checker..."
mypy src/ app.py

echo "Running linter..."
flake8 . --max-line-length=100

echo "Running tests with coverage..."
PYTHONPATH=$PYTHONPATH:$(pwd) pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=90
