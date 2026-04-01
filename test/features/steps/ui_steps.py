from behave import when, then
from playwright.sync_api import sync_playwright

@when('I login to the storefront')
def step_login(context):
    playwright =sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

    context.page.goto("https://www.saucedemo.com/")
    context.page.fill("#user-name", "standard_user")
    context.page.fill("#password","secret_sauce")
    context.page.click("#login-button")

@when('I add a product to the cart')
def step_add_product(context):
    context.page.click(".inventory_item:first-child .btn_inventory")

@when('I checkout using data from the created pet')
def step_checkout(context):
    context.page.click(".shopping_cart_link")
    context.page.click("#checkout")

    context.page.fill("#first-name", context.pet_name)
    context.page.fill("#last-name", "Test")
    context.page.fill("#postal-code", str(context.pet_id))

    context.page.click("#continue")
    context.page.click("#finish")

@then('the order should be successfully placed')
def step_verify_order(context):
    confirmation_text = context.page.text_content(".complete-header")
    assert "Thank you for your order!" in confirmation_text

    context.browser.close()