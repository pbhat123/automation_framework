"""
core/utils.py

Reusable helper functions not tied to Selenium (timestamps, file/folder
naming, directory creation, config loading).
"""

import os
import importlib
from datetime import datetime


def get_timestamp():
    """Returns a filesystem-safe timestamp string, e.g. 20260825_143512."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def create_directory_if_not_exists(path):
    """Creates the directory (and parents) if it doesn't already exist."""
    os.makedirs(path, exist_ok=True)
    return path


def generate_report_filename(app_name, test_name):
    timestamp = get_timestamp()
    folder = os.path.join("reports", app_name)
    create_directory_if_not_exists(folder)
    return os.path.join(folder, f"{timestamp}_{app_name}_{test_name}_report.html")


def generate_log_filename(app_name, test_name):
    timestamp = get_timestamp()
    folder = os.path.join("logs", app_name)
    create_directory_if_not_exists(folder)
    return os.path.join(folder, f"{timestamp}_{app_name}_{test_name}.log")


def generate_screenshot_filename(app_name, test_name):
    timestamp = get_timestamp()
    folder = os.path.join("screenshots", app_name)
    create_directory_if_not_exists(folder)
    return os.path.join(folder, f"{timestamp}_{app_name}_{test_name}_FAILURE.png")


def read_config(app_name):
    """
    Dynamically loads an app's config module, e.g.:
    read_config("terminator") -> imports apps.terminator.config.terminator_config
    """
    module_path = f"apps.{app_name}.config.{app_name}_config"
    return importlib.import_module(module_path)
