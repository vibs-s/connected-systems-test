class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, value):
        self.page.locator(selector).fill(value)

    def get_text(self, selector):
        return self.page.locator(selector).text_content()