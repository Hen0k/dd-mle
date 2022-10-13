import logging
from datetime import datetime
import os

from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger


def get_rotating_log(filename: str,
                     logger_name: str,
                     filepath: str = None) -> logging.Logger:
    """Creates a rotating log object that writes to a file and the console"""

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)


    # add a rotating handler
    if not filepath:
        path = os.path.join('logs', filename)
        print(path)
    else: 
        path = os.path.join(filepath, filename)
    rot_handler = RotatingFileHandler(path,
                                      maxBytes=1000000,
                                      backupCount=1)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    # f_format = logging.Formatter(
        # '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # console_handler.setFormatter(c_format)
    
    logger.addHandler(console_handler)

    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    rot_handler.setFormatter(formatter)

    logger.addHandler(rot_handler)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger