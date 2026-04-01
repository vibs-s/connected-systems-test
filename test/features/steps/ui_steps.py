from behave import when, then
from test.pages.login_page import LoginPage
from test.pages.products_page import ProductsPage
from test.pages.checkout_page import CheckoutPage
from test.utils.config import BASE_URL, USERNAME, PASSWORD


@when("I login to the storefront")
def step_login(context):
    login_page = LoginPage(context.page)
    login_page.load(BASE_URL)
    login_page.login(USERNAME, PASSWORD)


@when("I add a product to the cart")
def step_add_product(context):
    products_page = ProductsPage(context.page)
    products_page.add_first_product()
    products_page.go_to_cart()


@when("I checkout using data from the created pet")
def step_checkout(context):
    context.page.click("#checkout")

    checkout_page = CheckoutPage(context.page)

    checkout_page.fill_details(
        first_name=context.pet_name,
        last_name="Test",
        postal_code=str(context.pet_id),
    )

    checkout_page.finish_order()


@then("the order should be successfully placed")
def step_verify_order(context):
    checkout_page = CheckoutPage(context.page)
    confirmation_text = checkout_page.get_success_message()

    assert "Thank you for your order!" in confirmation_text