from selene import browser
from selene.support.conditions import be


def test_fill_fields():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("#firstName").should(be.blank).type('Uladzislau')
    browser.element("#lastName").should(be.blank).type('Makhakhei')
    browser.element("#userEmail").should(be.blank).type('vladqaguru@gmail.com')
    browser.all('.custom-control-label')[0].click()
    browser.element("#userNumber").should(be.blank).type('2055551215')
    browser.element("#dateOfBirthInput").clear()
