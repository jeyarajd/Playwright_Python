from pages.buttons_page import ButtonsPage
from pages.forms_page import FormsPage
from pages.home_page import HomePage
from pages.windows_page import WindowsPage


def test_home_page_navigation(page):
    home_page = HomePage(page)
    home_page.open_home()
    assert home_page.heading_text() == "Learning Playground"
    home_page.open_forms_page()
    assert "forms.html" in page.url


def test_form_submission(page):
    forms_page = FormsPage(page)
    forms_page.open_forms_page()
    forms_page.submit_form("Ada Lovelace", "ada@example.com")
    output = forms_page.output_text()
    assert "Ada Lovelace" in output
    assert "ada@example.com" in output


def test_primary_button_click(page):
    buttons_page = ButtonsPage(page)
    buttons_page.open_buttons_page()
    buttons_page.click_primary_button()
    assert buttons_page.output_text() == "Primary button clicked"


def test_new_window_opens(page):
    windows_page = WindowsPage(page)
    windows_page.open_windows_page()
    with page.context.expect_event("page") as popup_info:
        windows_page.open_new_window()
    popup = popup_info.value
    assert "popup.html" in popup.url
    assert "Popup window opened" in popup.locator("h1").text_content()
