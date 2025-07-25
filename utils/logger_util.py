import logging
import os
from datetime import datetime

def create_logger(logger_name):
    log_dir="logs"
    os.makedirs(log_dir,exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log_file=os.path.join(log_dir,f"{logger_name}_{timestamp}.log")
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    #Formmatter
    formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")

    # File handler
    file_handler =logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # avoid adding duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger