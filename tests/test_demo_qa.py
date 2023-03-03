from selene import browser, be, by


def test_fill_fields(browser_setup):
    browser.element("#firstName").should(be.blank).type('Uladzislau')  # fill First name field
    browser.element("#lastName").should(be.blank).type('Makhakhei')  # fill Last name field
    browser.element("#userEmail").should(be.blank).type('vladqaguru@gmail.com')  # fill email field
    browser.element('.custom-control label[for="gender-radio-1"]').click()  # choose gender
    browser.element("#userNumber").should(be.blank).type('2055551215')  # fill number field
    browser.element('#dateOfBirthInput').click()  # open calendar
    browser.element('.react-datepicker__month-select option[value="6"]').click()  # choose month
    browser.element('.react-datepicker__year-select option[value="1994"]').click()  # choose year
    browser.element('.react-datepicker__day--003').click()
    # choose day
    browser.element('#subjectsInput').type('Maths').press_enter()
    # select subjects
    browser.element('#hobbiesWrapper label[for="hobbies-checkbox-3"]').click()
    # select hobbies
    browser.element('.form-control-file').send_keys('tests/resources/picture.jpg')

