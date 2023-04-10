import pytest
from selene.support.shared import browser

DEFAULT_BROWSER_VERSION = "100.0"


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = True
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
