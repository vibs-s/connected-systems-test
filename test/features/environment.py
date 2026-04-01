from playwright.sync_api import sync_playwright
from test.utils.config import HEADLESS


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()