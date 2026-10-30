from pages.base_page import BasePage


class FormsPage(BasePage):
    def open_forms_page(self):
        self.open("/forms.html")

    def submit_form(self, full_name: str, email: str):
        self.fill("#full-name", full_name)
        self.fill("#email", email)
        self.click("#submit-form")

    def output_text(self) -> str:
        return self.text("#form-output")
