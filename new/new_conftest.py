"""
conftest.py

Shared pytest fixtures and hooks for all apps/tests:
- driver fixture (Edge, headed)
- actions fixture (BaseActions wrapper)
- per-test log file
- timestamped HTML report per run
- screenshot capture on failure, attached to the HTML report
"""

import os
import logging
import pytest

from core.driver_factory import get_driver, quit_driver
from core.base_actions import BaseActions
from core.utils import (
    get_timestamp,
    create_directory_if_not_exists,
    generate_log_filename,
    generate_screenshot_filename,
)


def _get_app_name(request):
    """
    Derives the app name from the test's file path, e.g.
    apps/terminator/tests/integration/test_login.py -> 'terminator'
    """
    path_parts = request.fspath.strpath.replace("\\", "/").split("/")
    if "apps" in path_parts:
        idx = path_parts.index("apps")
        return path_parts[idx + 1]
    return "unknown_app"


# ---------------- TIMESTAMPED HTML REPORT PER RUN ----------------
def pytest_configure(config):
    if not config.option.htmlpath:
        timestamp = get_timestamp()

        # Try to detect the app name from the invoked test path (e.g. apps/terminator/...)
        app_name = "unknown_app"
        for arg in config.args:
            parts = arg.replace("\\", "/").split("/")
            if "apps" in parts:
                idx = parts.index("apps")
                if idx + 1 < len(parts):
                    app_name = parts[idx + 1]
                    break

        report_dir = create_directory_if_not_exists(os.path.join("reports", app_name))
        config.option.htmlpath = os.path.join(report_dir, f"{timestamp}_{app_name}_test_report.html")
        config.option.self_contained_html = True


# ---------------- DRIVER / ACTIONS FIXTURES ----------------
@pytest.fixture
def driver(request):
    app_name = _get_app_name(request)
    test_name = request.node.name

    web_driver = get_driver()

    # Per-test logging setup
    log_file = generate_log_filename(app_name, test_name)
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f"Starting test: {test_name} for app: {app_name}")

    # Attach to the test node for use in the failure/screenshot hook below
    request.node.web_driver = web_driver
    request.node.app_name = app_name
    request.node.logger = logger

    yield web_driver

    logger.info(f"Finished test: {test_name}")
    logger.removeHandler(file_handler)
    file_handler.close()

    quit_driver(web_driver)


@pytest.fixture
def actions(driver):
    return BaseActions(driver)


# ---------------- SCREENSHOT ON FAILURE ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        web_driver = getattr(item, "web_driver", None)
        app_name = getattr(item, "app_name", "unknown_app")
        test_name = item.name

        if web_driver:
            screenshot_path = generate_screenshot_filename(app_name, test_name)
            try:
                web_driver.save_screenshot(screenshot_path)

                # Attach screenshot to the pytest-html report, if the plugin is active
                if hasattr(item.config, "_html"):
                    from pytest_html import extras
                    extra = getattr(report, "extra", [])
                    extra.append(extras.image(screenshot_path))
                    report.extra = extra

            except Exception as e:
                print(f"Failed to capture screenshot: {e}")


def pytest_html_report_title(report):
    report.title = "Automation Test Report"
