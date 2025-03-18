import logging

# Configure logging
logging.basicConfig(
    filename="test_log.log",  # Save logs to this file
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Create a logger instance
logger = logging.getLogger(__name__)
