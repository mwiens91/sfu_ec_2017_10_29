"""Contains a logger to print results to console/file."""

import time
import logging

def initialize_log():
    """Initializes the logger."""
    logging.basicConfig(
        filename='result.txt',
        filemode='a',
        format='%(asctime)s,%(msecs)d - %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    logging.info('##### Log Initialized #####')

def log(message):
    """Logs a message to the logger."""
    logging.info(message)
    print(message)
