from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/") -> None:
        self.page.goto(f"http://127.0.0.1:3001{path}")

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str) -> None:
        self.page.locator(selector).fill(value)

    def text(self, selector: str) -> str:
        value = self.page.locator(selector).text_content()
        return value.strip() if value else ""

    def current_url(self) -> str:
        return self.page.url
