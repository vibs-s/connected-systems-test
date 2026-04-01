from test.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"
    SUCCESS_MSG = ".complete-header"

    def fill_details(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    def finish_order(self):
        self.click(self.FINISH)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)