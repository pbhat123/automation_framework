"""
core/base_actions.py

Reusable Selenium action methods used by all Page Object Model (POM) files
across all apps. This is the ONLY file that should contain raw Selenium
syntax. Page objects call these methods instead of using Selenium directly.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

DEFAULT_TIMEOUT = 10

LOCATOR_MAP = {
    "id": By.ID,
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
    "name": By.NAME,
    "class": By.CLASS_NAME,
    "tag": By.TAG_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
}


class BaseActions:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.logger = logger

    # ---------------- INTERNAL HELPERS ----------------
    def _log(self, message):
        if self.logger:
            self.logger.info(message)

    def _by(self, locator):
        """Converts ('xpath', 'value') into (By.XPATH, 'value')."""
        locator_type, locator_value = locator
        by_type = LOCATOR_MAP.get(locator_type.lower())
        if by_type is None:
            raise ValueError(f"Unsupported locator type: {locator_type}")
        return by_type, locator_value

    def _find(self, locator, timeout=DEFAULT_TIMEOUT):
        by_type, value = self._by(locator)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by_type, value))
        )

    def _find_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        by_type, value = self._by(locator)
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by_type, value))
        )

    def _find_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        by_type, value = self._by(locator)
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by_type, value))
        )

    # ================= NAVIGATION =================
    def open_url(self, url):
        self._log(f"Opening URL: {url}")
        self.driver.get(url)

    def refresh_page(self):
        self._log("Refreshing page")
        self.driver.refresh()

    def go_back(self):
        self._log("Navigating back")
        self.driver.back()

    def go_forward(self):
        self._log("Navigating forward")
        self.driver.forward()

    def get_current_url(self):
        url = self.driver.current_url
        self._log(f"Current URL: {url}")
        return url

    def get_page_title(self):
        title = self.driver.title
        self._log(f"Page title: {title}")
        return title

    # ================= TEXT / INPUT FIELDS =================
    def enter_text(self, locator, text):
        self._log(f"Entering text '{text}' into {locator}")
        element = self._find_visible(locator)
        element.clear()
        element.send_keys(text)

    def enter_password(self, locator, password):
        self._log(f"Entering password into {locator}")
        element = self._find_visible(locator)
        element.clear()
        element.send_keys(password)

    def clear_text(self, locator):
        self._log(f"Clearing text in {locator}")
        self._find_visible(locator).clear()

    def append_text(self, locator, text):
        self._log(f"Appending text '{text}' to {locator}")
        self._find_visible(locator).send_keys(text)

    def get_text(self, locator):
        text = self._find_visible(locator).text
        self._log(f"Got text '{text}' from {locator}")
        return text

    def get_attribute(self, locator, attr_name):
        value = self._find(locator).get_attribute(attr_name)
        self._log(f"Got attribute '{attr_name}'='{value}' from {locator}")
        return value

    # ================= CLICKS =================
    def click(self, locator):
        self._log(f"Clicking {locator}")
        self._find_clickable(locator).click()

    def double_click(self, locator):
        self._log(f"Double-clicking {locator}")
        element = self._find_clickable(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        self._log(f"Right-clicking {locator}")
        element = self._find_clickable(locator)
        ActionChains(self.driver).context_click(element).perform()

    def click_using_js(self, locator):
        self._log(f"JS-clicking {locator}")
        element = self._find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # ================= DROPDOWNS =================
    def select_dropdown_by_text(self, locator, value):
        self._log(f"Selecting dropdown option '{value}' (by text) in {locator}")
        Select(self._find_visible(locator)).select_by_visible_text(value)

    def select_dropdown_by_index(self, locator, index):
        self._log(f"Selecting dropdown option at index {index} in {locator}")
        Select(self._find_visible(locator)).select_by_index(index)

    def select_dropdown_by_value(self, locator, value):
        self._log(f"Selecting dropdown option '{value}' (by value) in {locator}")
        Select(self._find_visible(locator)).select_by_value(value)

    def get_selected_dropdown_option(self, locator):
        option = Select(self._find_visible(locator)).first_selected_option.text
        self._log(f"Currently selected dropdown option in {locator}: '{option}'")
        return option

    # ================= CHECKBOXES / RADIO =================
    def select_checkbox(self, locator):
        self._log(f"Selecting checkbox {locator}")
        element = self._find_clickable(locator)
        if not element.is_selected():
            element.click()

    def deselect_checkbox(self, locator):
        self._log(f"Deselecting checkbox {locator}")
        element = self._find_clickable(locator)
        if element.is_selected():
            element.click()

    def is_checkbox_selected(self, locator):
        selected = self._find(locator).is_selected()
        self._log(f"Checkbox {locator} selected: {selected}")
        return selected

    def select_radio_button(self, locator):
        self._log(f"Selecting radio button {locator}")
        element = self._find_clickable(locator)
        if not element.is_selected():
            element.click()

    # ================= DATE PICKERS =================
    def select_date(self, locator, date_value):
        """For simple text-input based date fields."""
        self._log(f"Entering date '{date_value}' into {locator}")
        element = self._find_visible(locator)
        element.clear()
        element.send_keys(date_value)

    def select_date_from_calendar_widget(self, locator, day, month, year):
        """
        Placeholder for calendar-widget-based date pickers.
        Calendar widgets vary a lot between apps, so this method is meant
        to be customized per app if a graphical calendar is used.
        """
        self._log(f"Attempting calendar widget date selection: {day}/{month}/{year} in {locator}")
        raise NotImplementedError(
            "Customize select_date_from_calendar_widget() for this app's calendar widget."
        )

    # ================= FILE UPLOAD =================
    def upload_file(self, locator, file_path):
        self._log(f"Uploading file '{file_path}' via {locator}")
        element = self._find(locator)
        element.send_keys(file_path)

    # ================= WAITS =================
    def wait_for_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        self._log(f"Waiting for {locator} to be visible (timeout={timeout}s)")
        self._find_visible(locator, timeout)

    def wait_for_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        self._log(f"Waiting for {locator} to be clickable (timeout={timeout}s)")
        self._find_clickable(locator, timeout)

    def wait_for_element_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        self._log(f"Waiting for {locator} to be invisible (timeout={timeout}s)")
        by_type, value = self._by(locator)
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((by_type, value))
        )

    def wait_for_page_load(self, timeout=DEFAULT_TIMEOUT):
        self._log(f"Waiting for page load (timeout={timeout}s)")
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    # ================= VALIDATIONS / STATE CHECKS =================
    def is_displayed(self, locator):
        try:
            result = self._find(locator).is_displayed()
        except Exception:
            result = False
        self._log(f"is_displayed check on {locator}: {result}")
        return result

    def is_enabled(self, locator):
        result = self._find(locator).is_enabled()
        self._log(f"is_enabled check on {locator}: {result}")
        return result

    def is_selected(self, locator):
        result = self._find(locator).is_selected()
        self._log(f"is_selected check on {locator}: {result}")
        return result

    # ================= MOUSE / KEYBOARD ACTIONS =================
    def hover_over_element(self, locator):
        self._log(f"Hovering over {locator}")
        element = self._find_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        self._log(f"Dragging from {source_locator} to {target_locator}")
        source = self._find_visible(source_locator)
        target = self._find_visible(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def press_key(self, locator, key):
        """key: pass a Selenium Keys attribute name as string, e.g. 'ENTER', 'TAB'."""
        self._log(f"Pressing key '{key}' on {locator}")
        element = self._find_visible(locator)
        key_value = getattr(Keys, key.upper(), key)
        element.send_keys(key_value)

    def scroll_to_element(self, locator):
        self._log(f"Scrolling to {locator}")
        element = self._find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_by_pixels(self, x, y):
        self._log(f"Scrolling by ({x}, {y}) pixels")
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    # ================= ALERTS (JS POPUPS) =================
    def accept_alert(self, timeout=DEFAULT_TIMEOUT):
        self._log("Accepting alert")
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self, timeout=DEFAULT_TIMEOUT):
        self._log("Dismissing alert")
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        text = self.driver.switch_to.alert.text
        self._log(f"Alert text: '{text}'")
        return text

    def enter_text_in_alert(self, text, timeout=DEFAULT_TIMEOUT):
        self._log(f"Entering text '{text}' into alert")
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        self.driver.switch_to.alert.send_keys(text)

    # ================= FRAMES / WINDOWS =================
    def switch_to_frame(self, locator):
        self._log(f"Switching to frame {locator}")
        element = self._find(locator)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self._log("Switching to default content")
        self.driver.switch_to.default_content()

    def switch_to_window(self, window_handle):
        self._log(f"Switching to window {window_handle}")
        self.driver.switch_to.window(window_handle)

    def get_all_window_handles(self):
        handles = self.driver.window_handles
        self._log(f"Window handles: {handles}")
        return handles

    def close_current_window(self):
        self._log("Closing current window")
        self.driver.close()

    # ================= SCREENSHOTS =================
    def take_screenshot(self, file_path):
        self._log(f"Taking screenshot: {file_path}")
        self.driver.save_screenshot(file_path)

    # ================= TABLE HANDLING =================
    def get_table_row_count(self, locator):
        table = self._find_visible(locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        self._log(f"Table {locator} row count: {len(rows)}")
        return len(rows)

    def get_table_cell_data(self, locator, row, col):
        table = self._find_visible(locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        cells = rows[row].find_elements(By.TAG_NAME, "td")
        value = cells[col].text
        self._log(f"Table {locator} cell [{row}][{col}]: '{value}'")
        return value

    # ================= MULTI-SELECT =================
    def select_multiple_dropdown_options(self, locator, values_list):
        self._log(f"Selecting multiple dropdown options {values_list} in {locator}")
        select = Select(self._find_visible(locator))
        for value in values_list:
            select.select_by_visible_text(value)
