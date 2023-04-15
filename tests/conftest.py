import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.attach import add_logs, add_html, add_screenshot


@pytest.fixture(scope='session')
def browser_setup():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": False},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    browser = Browser(Config(driver))

    yield browser

    add_html(browser)
    add_screenshot(browser)
    add_logs(browser)
