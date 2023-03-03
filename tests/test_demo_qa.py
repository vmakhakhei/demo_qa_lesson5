import pytest
from selene import browser, be, have, by


def test_fill_fields(browser_setup):
    browser.element("#firstName").should(be.blank).type('Uladzislau')
    browser.element("#lastName").should(be.blank).type('Makhakhei')
    browser.element("#userEmail").should(be.blank).type('vladqaguru@gmail.com')
    browser.element('div[class*="custom-control"] label[for="gender-radio-1"]').click()
    browser.element("#userNumber").should(be.blank).type('2055551215')
    browser.element(by.id('dateOfBirthInput')).click()
    browser.element('select[class="react-datepicker__month-select"] option[value="6"]').click()
    browser.element('select[class="react-datepicker__year-select"] option[value="1994"]').click()
    browser.element('div[class="react-datepicker__day react-datepicker__day--003 react-datepicker__day--weekend"]').click()
    browser.element('div[id="subjectsContainer"] input[id="subjectsInput"]').type('Maths').press_enter()
    browser.element('div[id="hobbiesWrapper"] label[for="hobbies-checkbox-3"]').click()
    browser.element(by.id("uploadPicture")).send_keys('C:\Users\Anastasya\PycharmProjects\demo_qa_lesson5\picture.jpg')