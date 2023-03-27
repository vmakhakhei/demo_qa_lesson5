from selene import browser, be, have, by
import os

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, name):
        browser.element("#firstName").should(be.blank).type(name)

    def fill_last_name(self, surname):
        browser.element("#lastName").should(be.blank).type(surname)

    def fill_email(self, email):
        browser.element("#userEmail").should(be.blank).type(email)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f".react-datepicker__month-select").type(month)
        browser.element(f'''.react-datepicker__year-select option[value="{year}"]''').click()
        browser.element(f'''.react-datepicker__day--0{day}''').click()

    def assert_registred_user_info(self, name, email, gender, phone, date, subjects, hobbies, avatar, address,
                                   city_option):
        browser.element('.table').all('td').even.should(
            have.exact_texts(name, email, gender, phone, date, subjects, hobbies, avatar, address, city_option,))

    def gender(self, gender):
        if gender.lower() == 'male':
            browser.element('[for=gender-radio-1]').click()
        elif gender.lower() == 'female':
            browser.element('[for=gender-radio-2]').click()
        elif gender.lower() == 'other':
            browser.element('[for=gender-radio-3]').click()
        else:
            raise AttributeError

    def type_phone(self, phone_number):
        browser.element("#userNumber").should(be.blank).type(phone_number)

    def click_submit(self):
        browser.execute_script("document.querySelector('#submit').click()")

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').should(be.blank).type(current_address)
        pass

    def select_state(self, state):
        browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()

    def select_city(self, city):
        browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()

    def upload_picture(self, picture_path):
        browser.element(by.id('uploadPicture')).send_keys(os.getcwd() + picture_path)

    def select_subjects(self, subjects):
        browser.element('#subjectsInput').should(be.blank).type(subjects).press_enter()

    def select_hobbies(self, hobbies):
        if hobbies.lower() == 'music':
            browser.element('#hobbiesWrapper label[for="hobbies-checkbox-3"]').click()
        elif hobbies.lower() == 'reading':
            browser.element('#hobbiesWrapper label[for="hobbies-checkbox-2"]').click()
        elif hobbies.lower() == 'sports':
            browser.element('#hobbiesWrapper label[for="hobbies-checkbox-1"]').click()
        else:
            raise AttributeError