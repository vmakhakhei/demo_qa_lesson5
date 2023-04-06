import allure
from selene import browser, be, have
import os

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender_male = browser.element('[for=gender-radio-1]')
        self.gender_woman = browser.element('[for=gender-radio-2]')
        self.gender_other = browser.element('[for=gender-radio-3]')
        self.user_number = browser.element("#userNumber")
        self.current_adress = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.subjects = browser.element('#subjectsInput')
        self.hobby_sports = browser.element(
            '#hobbiesWrapper label[for="hobbies-checkbox-1"]'
        )
        self.hobby_reading = browser.element(
            '#hobbiesWrapper label[for="hobbies-checkbox-2"]'
        )
        self.hobby_music = browser.element(
            '#hobbiesWrapper label[for="hobbies-checkbox-3"]'
        )
        self.upload_picture_element = browser.element('#uploadPicture')
        self.open_calendar = browser.element('#dateOfBirthInput')
        self.assert_modal = browser.element('.table')

    @allure.step('Open registration page')
    def open(self, page):
        browser.open(page)

    @allure.step('Fill the First Name field')
    def fill_first_name(self, name):
        self.first_name.should(be.blank).type(name)

    @allure.step('Fill the Last Name field')
    def fill_last_name(self, surname):
        self.last_name.should(be.blank).type(surname)

    @allure.step('Fill the Email field')
    def fill_email(self, email):
        self.email.should(be.blank).type(email)

    @allure.step('Fill the date of birth')
    def fill_date_of_birth(self, day, month, year):
        self.open_calendar.click()
        browser.element(f".react-datepicker__month-select").type(month)
        assert month.title() in months, "Введено некорректное значение"
        browser.element(
            f'''.react-datepicker__year-select option[value="{year}"]'''
        ).click()
        assert len(str(day)) == 2, "Введите дату двузначиным значением"
        browser.element(f'''.react-datepicker__day--0{day}''').click()

    @allure.step('Assert registred user information ')
    def assert_registred_user_info(
        self,
        name,
        email,
        gender,
        phone,
        date,
        subjects,
        hobbies,
        avatar,
        address,
        city_option,
    ):
        self.assert_modal.all('td').even.should(
            have.exact_texts(
                name,
                email,
                gender,
                phone,
                date,
                subjects,
                hobbies,
                avatar,
                address,
                city_option,
            )
        )

    @allure.step('Select gender')
    def gender(self, gender):
        if gender.lower() == 'male':
            self.gender_male.click()
        elif gender.lower() == 'female':
            self.gender_woman.click()
        elif gender.lower() == 'other':
            self.gender_other.click()
        else:
            raise AttributeError

    @allure.step('Fill phone field')
    def type_phone(self, phone_number):
        self.user_number.should(be.blank).type(phone_number)

    @allure.step('Click the submit button')
    def submit(self):
        browser.execute_script("document.querySelector('#submit').click()")

    @allure.step('Fill current address field')
    def fill_current_address(self, current_address):
        self.current_adress.should(be.blank).type(current_address)
        pass

    @allure.step('Select State')
    def select_state(self, state):
        self.state.should(be.blank).type(state).press_enter()

    @allure.step('Select City')
    def select_city(self, city):
        self.city.should(be.blank).type(city).press_enter()

    @allure.step('Upload image')
    def upload_avatar(self, image):
        self.upload_picture_element.send_keys(os.getcwd() + f'\\resources\\{image}')

    @allure.step('Select subjects')
    def select_subjects(self, subjects):
        self.subjects.should(be.blank).type(subjects).press_enter()

    @allure.step('Select hobbies')
    def select_hobbies(self, hobbies):
        if hobbies.lower() == 'music':
            self.hobby_music.click()
        elif hobbies.lower() == 'reading':
            self.hobby_reading.click()
        elif hobbies.lower() == 'sports':
            self.hobby_sports.click()
        else:
            raise AttributeError
