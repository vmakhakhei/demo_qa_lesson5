from selene import browser, be, by, have

first_name = 'Uladzislau'
last_name = 'Makhakhei'
email = 'vladqaguru@gmail.com'
gender = '1'  # 1-male, 2-female, 3-other

if gender == '1':
    gender_print = 'Male'
elif gender == '2':
    gender_print = 'Female'
elif gender == '3':
    gender_print = 'Other'

phone_number = '2055551215'
month = '6'  # month of birthday-1
year = '1994'  # year of birthday
day = '03'  # day of birthday
FILE = 'C:\\Users\\Anastasya\\PycharmProjects\\demo_qa_lesson5\\resources\\picture.jpg'  # path to file
current_adress = 'Minsk'


def test_fill_fields(browser_setup):
    browser.open('/automation-practice-form')
    browser.element("#firstName").should(be.blank).type(first_name)  # fill First name field
    browser.element("#lastName").should(be.blank).type(last_name)  # fill Last name field
    browser.element("#userEmail").should(be.blank).type(email)  # fill email field
    browser.element(f'.custom-control label[for="gender-radio-{gender}"]').click()  # choose gender
    browser.element("#userNumber").should(be.blank).type(phone_number)  # fill number field
    browser.element('#dateOfBirthInput').click()  # open calendar
    browser.element(f'''.react-datepicker__month-select option[value="{month}"]''').click()  # choose month
    browser.element(f'''.react-datepicker__year-select option[value="{year}"]''').click()  # choose year
    browser.element(f'''.react-datepicker__day--0{day}''').click()
    # choose day
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    # select subjects
    browser.element('#hobbiesWrapper label[for="hobbies-checkbox-3"]').click()
    # select hobbies
    browser.element(by.id('uploadPicture')).send_keys(FILE)  # upload file
    browser.element('#currentAddress').should(be.blank).type(current_adress)  # fill adress
    browser.element('#react-select-3-input').should(be.blank).type('NCR').press_enter()  # select state
    browser.element('#react-select-4-input').should(be.blank).type('Noida').press_enter()  # select city
    browser.execute_script("document.querySelector('#submit').click()")  # click the button submit
    # check_inputed_data
    browser.all('.table-responsive tbody tr').should(have.size(10))
    browser.element('tr:nth-child(1) td:nth-child(2)').should(have.text(f'{first_name} {last_name}'))
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text(email))
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text(gender_print))
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text(phone_number))
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('03 July,1994'))
    browser.element('tr:nth-child(6) td:nth-child(2)').should(have.text('Maths'))
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Music'))
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text(current_adress))
    browser.element('tr:nth-child(10) td:nth-child(2)').should(have.text('NCR Noida'))
