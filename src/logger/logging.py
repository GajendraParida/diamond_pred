import logging
import os
from datetime import datetime

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_path = os.path.join(os.getcwd(), "logs")

# Create the log directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Define the full log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    filename=LOG_FILEPATH, 
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# Example usage of logging
logging.info("This is my second testing")
