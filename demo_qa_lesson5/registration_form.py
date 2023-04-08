import allure
from selene import browser, be, have
import os
from selene.support.shared import browser

from users.users import User

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
        self.month_of_birth = browser.element(f".react-datepicker__month-select")
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
        self._choose_hobby = browser.all('[for^=hobbies-checkbox]')
        self.upload_picture_element = browser.element('#uploadPicture')
        self.open_calendar = browser.element('#dateOfBirthInput')
        self.assert_modal = browser.element('.table')

    @allure.step('Open register page')
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, name):
        self.first_name.should(be.blank).type(name)

    def fill_last_name(self, surname):
        self.last_name.should(be.blank).type(surname)

    def fill_email(self, email):
        self.email.should(be.blank).type(email)

    def fill_birthday(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        self.month_of_birth.type(month)
        assert month.title() in months, "Введено некорректное значение"
        browser.element(
            f'''.react-datepicker__year-select option[value="{year}"]'''
        ).click()
        assert len(str(year)) == 4, 'Введено некорректное значение'
        browser.element(f'''.react-datepicker__day--0{day}''').click()
        assert len(str(day)) == 2, "Введите дату двузначиным значением"

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

    def gender(self, gender):
        if gender.lower() == 'male':
            self.gender_male.click()
        elif gender.lower() == 'female':
            self.gender_woman.click()
        elif gender.lower() == 'other':
            self.gender_other.click()
        else:
            raise AttributeError

    def type_phone(self, phone_number):
        self.user_number.should(be.blank).type(phone_number)

    @allure.step('Click submit button')
    def click_submit(self):
        browser.execute_script("document.querySelector('#submit').click()")

    def fill_current_address(self, current_address):
        self.current_adress.should(be.blank).type(current_address)
        pass

    def select_state(self, state):
        self.state.should(be.blank).type(state).press_enter()

    def select_city(self, city):
        self.city.should(be.blank).type(city).press_enter()

    def upload_avatar(self, name_picture):
        self.upload_picture_element.send_keys(
            f'{os.getcwd()}/resources/{name_picture}'
        )

    def select_subjects(self, subjects):
        for subject in subjects:
            self.subjects.should(be.blank).type(subject).press_enter()

    def choose_hobby(self, hobbies):
        for hobby in hobbies:
            browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()

    @allure.step('Filling info about user')
    def register(self, student: User):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.gender(student.gender)
        self.type_phone(student.phone_number)
        self.fill_birthday(
            student.day_of_birth, student.month_of_birth, student.year_of_birth
        )
        self.select_subjects(student.subjects)
        self.choose_hobby(student.hobbies)
        self.upload_avatar(student.name_picture)
        self.fill_current_address(student.adress)
        self.select_state(student.state)
        self.select_city(student.city)

    @allure.step('Assert inserted information')
    def assert_registred_user(self, student: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.email,
                student.gender,
                student.phone_number,
                f'{student.day_of_birth} {student.month_of_birth},{student.year_of_birth}',
                ', '.join(student.subjects),
                ', '.join(student.hobbies),
                student.name_picture,
                student.adress,
                f'{student.state} {student.city}',
            )
        )
