# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:11:06 2024.

@author: emmanuel.adoum & Rachel

@Module: Logger configuration for Solar System Simulation.

This module sets up a logger for tracking the simulation runs of the Solar
 System simulation. It employs a Singleton pattern to ensure that only one
 logger instance is created during the lifetime of the application.

The logger writes log messages to both the console and a log file,
 providing different levels of logging detail. A separator is added to
 distinguish between different simulation runs.
"""

import logging
from datetime import datetime

# Singleton pattern for logger
_logger_instance = None


def setup_logger(log_file='solar_system.log'):
    """
    Set up a logger for the Solar System simulation.

    This function initializes a logger that outputs messages to both
    the console and a specified log file. The logger is configured to
    provide different logging levels for console and file output.

    Args:
    ----
        log_file (str): The name of the log file to write log messages to.
        Defaults to 'solar_system.log'.

    Returns
    -------
        logging.Logger: A configured logger instance.

    The logger employs the Singleton pattern, ensuring only one instance
    is created and used throughout the application's runtime. This avoids
    duplicate log entries and ensures consistent logging behavior.
    """
    global _logger_instance
    if _logger_instance is not None:
        return _logger_instance

    logger = logging.getLogger('solar_system_logger')  # Unique logger name
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file)

        # Set levels for handlers
        console_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.DEBUG)

        # Create formatters and add them to handlers
        console_format = logging.Formatter('%(name)s - %(levelname)s\
                                           - %(message)s')
        file_format = logging.Formatter('%(asctime)s - %(name)s\
                                        - %(levelname)s - %(message)s')

        console_handler.setFormatter(console_format)
        file_handler.setFormatter(file_format)

        # Add handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    # Add a separator to distinguish different runs
    logger.info("=" * 50)
    logger.info(f"New Simulation Run at\
                {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 50)

    _logger_instance = logger
    return logger


# Access the logger via setup_logger()
logger = setup_logger()
