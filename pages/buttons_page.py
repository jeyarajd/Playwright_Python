from pages.base_page import BasePage


class ButtonsPage(BasePage):
    def open_buttons_page(self):
        self.open("/buttons.html")

    def click_primary_button(self):
        self.click("#primary-btn")

    def output_text(self) -> str:
        return self.text("#button-output")
