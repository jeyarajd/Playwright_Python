from pages.base_page import BasePage


class HomePage(BasePage):
    def open_home(self):
        self.open("/")

    def heading_text(self) -> str:
        return self.text("h1")

    def open_forms_page(self):
        self.page.locator("a[href='/forms.html']").click()
