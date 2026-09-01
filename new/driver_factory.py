"""
core/driver_factory.py

Handles Microsoft Edge WebDriver creation and teardown.
Currently configured for HEADED mode only, per project requirements.
"""

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver():
    """
    Creates and returns a Microsoft Edge WebDriver instance in headed mode.

    Uses Selenium's built-in Selenium Manager (Selenium 4.6+) to locate/
    download the correct msedgedriver automatically — no separate
    webdriver-manager package or manual driver download required.
    """
    options = EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Edge(options=options)

    return driver


def quit_driver(driver):
    """
    Safely quits the WebDriver instance.
    """
    if driver:
        driver.quit()
