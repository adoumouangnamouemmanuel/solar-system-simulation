# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:42:54 2024.

@author: emmanuel.adoum & Rachel

@Module: This module defines a function to load CSV data
 and provides error handling for common file-related issues.

This module contains the `load_file` function, which reads
 a CSV file and returns a list of dictionaries, where each dictionary
 represents a row in the CSV file. The module also includes error
 handling to manage potential issues related to file operations,
 such as file not found errors, permission errors, and CSV parsing errors.
"""

import csv
import logging
import os

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Create file handler and set level to debug
file_handler = logging.FileHandler('solar_system_simulation.log')
file_handler.setLevel(logging.DEBUG)
# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - \
                              %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Add file handler to logger
logger.addHandler(file_handler)


def load_file(file_path):
    """Load CSV file and return a list of dictionaries.

    Args:
    ----
        file_path (str): The path to the CSV file.

    Returns
    -------
        list: A list of dictionaries representing the rows in the CSV file.

    Raises
    ------
        FileNotFoundError: If the CSV file is not found.
        IOError: If there is an issue with reading the file.
        csv.Error: If there is an issue with parsing the CSV file.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}. Error: {e}")
        raise
    except IOError as e:
        logger.error(f"IO error while reading file: {file_path}. Error: {e}")
        raise
    except csv.Error as e:
        logger.error(f"CSV parsing error while reading file:\
                     {file_path}. Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred while reading file\
                     : {file_path}. Error: {e}")
        raise


# Load data from CSV
path = os.getcwd()
file_name = 'data.csv'
file_path = os.path.join(path, file_name)
try:
    lst = load_file(file_path)
except Exception as e:
    logger.error(f"Failed to load data from {file_path}. Error: {e}")
    # Ensure lst is defined to prevent further errors in main function
    lst = []
