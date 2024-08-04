# -*- coding: utf-8 -*-

"""
decorators.py. Decorators for enhancing functions with logging and performance.

Created on Sat Aug 3 18:12:29 2024

@author: emmanuel.adoum

@Module:

This module defines decorators that can be used to add logging and timing
functionality to any function in the app. The decorators provide insights
into function execution, helping with debugging and performance analysis.
"""

import time
from functools import wraps


def log_function_call(logger):
    """
    Thedecorator to log entry and exit of a function.

    This decorator logs messages when a function is entered and when
    it is exited. It is useful for tracing function calls and understanding
    the flow of execution within the application.

    Args:
    ----
        logger (logging.Logger): The logger object used to write log messages.

    Returns
    -------
        function: The wrapped function with added logging functionality.

    Example:
    -------
        @log_function_call(logger)
        def my_function():
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Entering {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"Exiting {func.__name__}")
            return result
        return wrapper
    return decorator


def measure_time(logger):
    """
    Thedecorator to measure the execution time of a function.

    This decorator calculates the time taken to execute a function and
    logs the execution duration. It is beneficial for identifying performance
    bottlenecks and optimizing code efficiency.

    Args:
    ----
        logger (logging.Logger): The logger object used to write debug
        messages with execution time details.

    Returns
    -------
        function: The wrapped function with added timing functionality.

    Example:
    -------
        @measure_time(logger)
        def my_function():
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            logger.debug(f"{func.__name__} executed in\
                         {end_time - start_time:.4f}s")
            return result
        return wrapper
    return decorator
