# LOGGER
# ----------------------------------------------------------------
# Imports
from globals import PATH

import os
os.chdir(PATH)

import logging

def createLogger(name = '', file = 'loggs.log',):
    logging.basicConfig(
            filename=file, 
            encoding='utf-8',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p', 
            filemode='w'
        )
    return logging.getLogger(name)
