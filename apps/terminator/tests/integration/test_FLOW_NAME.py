# apps/terminator/tests/integration/test_FLOW_NAME.py

# ============================================================
# WHAT YOU'LL MODIFY PER REAL TEST:
# 1. Delete sections/actions not used on that page/flow
# 2. Replace placeholder values ("SOME_OPTION", "MM/DD/YYYY", file paths)
#    with real data — pull from config where possible
# 3. Replace/adjust asserts to match real expected values
# 4. Reorder steps to match actual flow sequence
# 5. Uncomment sections (alerts, frames, tables, multi-select) only if
#    that flow needs them
# ============================================================

import pytest
from apps.terminator.pages.PAGE_NAME_page import PageNamePage
from apps.terminator.config import terminator_config as config


def test_FLOW_NAME(driver, actions):
    page = PageNamePage(driver, actions)

    # ---------------- NAVIGATION ----------------
    page.open_url(config.BASE_URL)
    page.wait_for_page_load()
    assert "EXPECTED_TITLE" in page.get_page_title(), "Page title mismatch"

    # ---------------- TEXT / INPUT FIELDS ----------------
    page.wait_for_element_visible()
    page.enter_text(config.TEXT_DATA_1)
    assert page.get_text() == config.TEXT_DATA_1, "Text entry failed"

    page.clear_text()
    page.append_text(config.TEXT_DATA_2)
    assert page.get_text() == config.TEXT_DATA_2, "Append text failed"

    # ---------------- PASSWORD ----------------
    page.enter_password(config.PASSWORD)
    # (no assert — password fields usually can't be read back)

    # ---------------- CLICKS ----------------
    page.wait_for_element_clickable()
    page.click()
    assert page.is_displayed(), "Element not displayed after click"

    # ---------------- DROPDOWNS ----------------
    page.wait_for_element_visible()
    page.select_dropdown_by_text("SOME_OPTION")
    assert page.get_selected_dropdown_option() == "SOME_OPTION", "Dropdown selection failed"

    # ---------------- CHECKBOX / RADIO ----------------
    page.select_checkbox()
    assert page.is_checkbox_selected(), "Checkbox not selected"

    page.select_radio_button()
    # (assert via is_selected() if needed)

    # ---------------- DATE PICKER ----------------
    page.select_date("MM/DD/YYYY")
    # (assert via get_text() or get_attribute() depending on field)

    # ---------------- FILE UPLOAD ----------------
    page.upload_file("C:\\path\\to\\file.pdf")
    # (assert via confirmation message element, if present)

    # ---------------- VALIDATIONS ----------------
    assert page.is_enabled(), "Element expected to be enabled"
    assert page.is_selected(), "Element expected to be selected"

    # ---------------- MOUSE / KEYBOARD ----------------
    page.hover_over_element()
    page.scroll_to_element()
    page.press_key("ENTER")

    # ---------------- ALERTS ----------------
    # page.accept_alert()
    # assert "EXPECTED_ALERT_TEXT" in page.get_alert_text()

    # ---------------- FRAMES / WINDOWS ----------------
    # page.switch_to_frame()
    # page.switch_to_default_content()

    # ---------------- TABLE ----------------
    # row_count = page.get_table_row_count()
    # assert row_count > 0, "Table has no rows"

    # ---------------- MULTI-SELECT ----------------
    # page.select_multiple_dropdown_options(["Option1", "Option2"])
