import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.attach import add_logs, add_html, add_screenshot


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='browser in which will be start tests',
        choices=['firefox', 'chrome'],
        default='chrome',
    )


@pytest.fixture(scope='function')
def browser_setup(request):
    browser_name = request.config.getoption('--browser')
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
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
