import logging

# Step 1: Create a logger
logger = logging.getLogger('sales_prediction_logger')
logger.setLevel(logging.DEBUG)  # Set the minimum logging level

# Step 2: Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Only show INFO level and above on the console

# Step 3: Create a file handler
file_handler = logging.FileHandler('sales_prediction.log')
file_handler.setLevel(logging.DEBUG)  # Log all levels to the file

# Step 4: Create a log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Step 5: Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage of the logger
logger.info("This is an INFO message.")
logger.debug("This is a DEBUG message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")
