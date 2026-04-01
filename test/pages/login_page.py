from test.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    def load(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)