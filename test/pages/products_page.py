from test.pages.base_page import BasePage


class ProductsPage(BasePage):
    FIRST_PRODUCT_ADD = ".inventory_item:first-child .btn_inventory"
    CART_ICON = ".shopping_cart_link"

    def add_first_product(self):
        self.click(self.FIRST_PRODUCT_ADD)

    def go_to_cart(self):
        self.click(self.CART_ICON)