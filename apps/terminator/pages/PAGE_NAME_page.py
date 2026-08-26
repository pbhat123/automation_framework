# apps/terminator/pages/PAGE_NAME_page.py

class PageNamePage:
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

        # ---------------- LOCATORS ----------------
        # Each element gets 2 locator options — keep the one that works, delete the other.
        # Primary = XPath (preferred). Alternate = ID/CSS/etc. (optional/backup).

        self.ELEMENT_1_XPATH = ("xpath", "//xpath_here_1")
        self.ELEMENT_1_ALT = ("id", "id_here_1")

        self.ELEMENT_2_XPATH = ("xpath", "//xpath_here_2")
        self.ELEMENT_2_ALT = ("id", "id_here_2")

        self.ELEMENT_3_XPATH = ("xpath", "//xpath_here_3")
        self.ELEMENT_3_ALT = ("id", "id_here_3")

        self.ELEMENT_4_XPATH = ("xpath", "//xpath_here_4")
        self.ELEMENT_4_ALT = ("id", "id_here_4")

        self.ELEMENT_5_XPATH = ("xpath", "//xpath_here_5")
        self.ELEMENT_5_ALT = ("id", "id_here_5")

    # ================= NAVIGATION =================
    def open_url(self, url):
        self.actions.open_url(url)

    def refresh_page(self):
        self.actions.refresh_page()

    def go_back(self):
        self.actions.go_back()

    def go_forward(self):
        self.actions.go_forward()

    def get_current_url(self):
        return self.actions.get_current_url()

    def get_page_title(self):
        return self.actions.get_page_title()

    # ================= TEXT / INPUT FIELDS =================
    def enter_text(self, value):
        self.actions.enter_text(self.ELEMENT_1_XPATH, value)

    def enter_password(self, value):
        self.actions.enter_password(self.ELEMENT_1_XPATH, value)

    def clear_text(self):
        self.actions.clear_text(self.ELEMENT_1_XPATH)

    def append_text(self, value):
        self.actions.append_text(self.ELEMENT_1_XPATH, value)

    def get_text(self):
        return self.actions.get_text(self.ELEMENT_1_XPATH)

    def get_attribute(self, attr_name):
        return self.actions.get_attribute(self.ELEMENT_1_XPATH, attr_name)

    # ================= CLICKS =================
    def click(self):
        self.actions.click(self.ELEMENT_2_XPATH)

    def double_click(self):
        self.actions.double_click(self.ELEMENT_2_XPATH)

    def right_click(self):
        self.actions.right_click(self.ELEMENT_2_XPATH)

    def click_using_js(self):
        self.actions.click_using_js(self.ELEMENT_2_XPATH)

    # ================= DROPDOWNS =================
    def select_dropdown_by_text(self, value):
        self.actions.select_dropdown_by_text(self.ELEMENT_3_XPATH, value)

    def select_dropdown_by_index(self, index):
        self.actions.select_dropdown_by_index(self.ELEMENT_3_XPATH, index)

    def select_dropdown_by_value(self, value):
        self.actions.select_dropdown_by_value(self.ELEMENT_3_XPATH, value)

    def get_selected_dropdown_option(self):
        return self.actions.get_selected_dropdown_option(self.ELEMENT_3_XPATH)

    # ================= CHECKBOXES / RADIO =================
    def select_checkbox(self):
        self.actions.select_checkbox(self.ELEMENT_4_XPATH)

    def deselect_checkbox(self):
        self.actions.deselect_checkbox(self.ELEMENT_4_XPATH)

    def is_checkbox_selected(self):
        return self.actions.is_checkbox_selected(self.ELEMENT_4_XPATH)

    def select_radio_button(self):
        self.actions.select_radio_button(self.ELEMENT_4_XPATH)

    # ================= DATE PICKERS =================
    def select_date(self, date_value):
        self.actions.select_date(self.ELEMENT_5_XPATH, date_value)

    def select_date_from_calendar_widget(self, day, month, year):
        self.actions.select_date_from_calendar_widget(self.ELEMENT_5_XPATH, day, month, year)

    # ================= FILE UPLOAD =================
    def upload_file(self, file_path):
        self.actions.upload_file(self.ELEMENT_1_XPATH, file_path)

    # ================= WAITS =================
    def wait_for_element_visible(self, timeout=10):
        self.actions.wait_for_element_visible(self.ELEMENT_1_XPATH, timeout)

    def wait_for_element_clickable(self, timeout=10):
        self.actions.wait_for_element_clickable(self.ELEMENT_1_XPATH, timeout)

    def wait_for_element_invisible(self, timeout=10):
        self.actions.wait_for_element_invisible(self.ELEMENT_1_XPATH, timeout)

    def wait_for_page_load(self, timeout=10):
        self.actions.wait_for_page_load(timeout)

    # ================= VALIDATIONS / STATE CHECKS =================
    def is_displayed(self):
        return self.actions.is_displayed(self.ELEMENT_1_XPATH)

    def is_enabled(self):
        return self.actions.is_enabled(self.ELEMENT_1_XPATH)

    def is_selected(self):
        return self.actions.is_selected(self.ELEMENT_1_XPATH)

    # ================= MOUSE / KEYBOARD ACTIONS =================
    def hover_over_element(self):
        self.actions.hover_over_element(self.ELEMENT_1_XPATH)

    def drag_and_drop(self, target_locator):
        self.actions.drag_and_drop(self.ELEMENT_1_XPATH, target_locator)

    def press_key(self, key):
        self.actions.press_key(self.ELEMENT_1_XPATH, key)

    def scroll_to_element(self):
        self.actions.scroll_to_element(self.ELEMENT_1_XPATH)

    def scroll_by_pixels(self, x, y):
        self.actions.scroll_by_pixels(x, y)

    # ================= ALERTS (JS POPUPS) =================
    def accept_alert(self):
        self.actions.accept_alert()

    def dismiss_alert(self):
        self.actions.dismiss_alert()

    def get_alert_text(self):
        return self.actions.get_alert_text()

    def enter_text_in_alert(self, text):
        self.actions.enter_text_in_alert(text)

    # ================= FRAMES / WINDOWS =================
    def switch_to_frame(self):
        self.actions.switch_to_frame(self.ELEMENT_1_XPATH)

    def switch_to_default_content(self):
        self.actions.switch_to_default_content()

    def switch_to_window(self, window_handle):
        self.actions.switch_to_window(window_handle)

    def get_all_window_handles(self):
        return self.actions.get_all_window_handles()

    def close_current_window(self):
        self.actions.close_current_window()

    # ================= SCREENSHOTS =================
    def take_screenshot(self, file_path):
        self.actions.take_screenshot(file_path)

    # ================= TABLE HANDLING =================
    def get_table_row_count(self):
        return self.actions.get_table_row_count(self.ELEMENT_1_XPATH)

    def get_table_cell_data(self, row, col):
        return self.actions.get_table_cell_data(self.ELEMENT_1_XPATH, row, col)

    # ================= MULTI-SELECT =================
    def select_multiple_dropdown_options(self, values_list):
        self.actions.select_multiple_dropdown_options(self.ELEMENT_3_XPATH, values_list)
