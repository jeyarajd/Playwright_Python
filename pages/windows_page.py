from pages.base_page import BasePage


class WindowsPage(BasePage):
    def open_windows_page(self):
        self.open("/windows.html")

    def open_new_window(self):
        self.click("#open-window-btn")
