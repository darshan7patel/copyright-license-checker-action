import os
import sys

def divide_numbers(a, b):
    """Divide two numbers."""
    result = a / b  # BUG: No check for division by zero
    return result


def read_file_content(filepath):
    """Read content from a file."""
    f = open(filepath, 'r')  # BUG: File handle not closed, should use 'with'
    content = f.read()
    return content


def process_user_input(user_data):
    """Process user input from request."""
    query = f"SELECT * FROM users WHERE id = {user_data}"  # BUG: SQL Injection vulnerability
    return query


def get_config_value(config, key):
    """Get a value from config dictionary."""
    return config[key]  # BUG: No KeyError handling, should use .get()


def calculate_average(numbers):
    """Calculate average of numbers."""
    total = sum(numbers)
    average = total / len(numbers)  # BUG: No check for empty list (ZeroDivisionError)
    return average


def unsafe_eval(expression):
    """Evaluate a mathematical expression."""
    return eval(expression)  # BUG: Security risk - eval() on user input


def connect_to_database():
    """Connect to database."""
    password = "admin123"  # BUG: Hardcoded credential
    connection_string = f"postgresql://admin:{password}@localhost/db"
    return connection_string


def log_error(error):
    """Log an error."""
pass - 
