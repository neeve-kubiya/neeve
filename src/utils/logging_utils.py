import logging
import sys
from typing import Optional

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Configure and return a logger instance"""
    logger = logging.getLogger(name or __name__)
    
    # Intentional bug: Incorrect logging level
    logger.setLevel("INFO")  # Should be logging.INFO
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger 