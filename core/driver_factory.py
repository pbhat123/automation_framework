"""
core/driver_factory.py

Handles Microsoft Edge WebDriver creation and teardown.
Currently configured for HEADED mode only, per project requirements.
"""

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver():
    """
    Creates and returns a Microsoft Edge WebDriver instance in headed mode.
    """
    options = EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--remote-allow-origins=*")

    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    return driver


def quit_driver(driver):
    """
    Safely quits the WebDriver instance.
    """
    if driver:
        driver.quit()
