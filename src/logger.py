import logging
import os
from datetime import datetime

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory path
logs_dir = os.path.join(os.getcwd(), "logs")  # Corrected path usage
os.makedirs(logs_dir, exist_ok=True)  # Create 'logs' directory if it doesn't exist

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Removed parentheses
)






