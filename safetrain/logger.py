import os
import sys
import time
import logging

def initialize_log():
	logging.basicConfig(
		filename='result.txt',
		filemode='a',
		format='%(asctime)s,%(msecs)d - %(message)s',
        	datefmt='%H:%M:%S',
        	level=logging.DEBUG)
	logging.info('##### Log Initialized #####')

def log(message):
	logging.info(message)
	print(message)
