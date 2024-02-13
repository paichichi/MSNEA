import os
import logging


def set_logger():
    filename = 'C:\\Users\\96446\\Documents\\GitHub\\MSNEA\\logs\\202402131243.log'
    log_directory = os.path.dirname(filename)

    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Proceed with setting up your logger
    logger = logging.getLogger()
    file_handler = logging.FileHandler(filename, mode='a', encoding='utf-8', delay=False)
    logger.addHandler(file_handler)

    return logger


logger = set_logger()
