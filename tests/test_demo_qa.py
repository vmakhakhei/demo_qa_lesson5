import allure
from demo_qa_lesson5 import registration_form
from users.users import User, Subjects, Hobbies

student = User(
    first_name="Uladzislau",
    last_name="Makhakhei",
    email="vladqaguru@gmail.com",
    day_of_birth="03",
    month_of_birth="July",
    year_of_birth="1994",
    gender="Male",
    phone_number="2055551215",
    subjects=[Subjects.maths.value, Subjects.biology.value],
    hobbies=[Hobbies.Music.value, Hobbies.Sports.value],
    name_picture="picture.jpg",
    adress="Minsk",
    state="NCR",
    city="Noida",
)


@allure.title("All Fields filled")
def test_fill_all_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.register(student)
    registration_page.click_submit()
    # THEN
    registration_page.assert_registred_user(student)


@allure.title("Submit Empty Form")
def test_submit_empty_form(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.click_submit()

    # THEN
    registration_page.validation_last_name()
    registration_page.validation_first_name()
    registration_page.validation_gender()
    registration_page.validation_phone()


@allure.title("Fill Only required fields")
def test_fill_required_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()

    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.gender(student.gender)
    registration_page.type_phone(student.phone_number)

    registration_page.click_submit()

    # THEN
    registration_page.check_registred_data(student.first_name).check_registred_data(
            student.last_name
        ).check_registred_data(student.gender).check_registred_data(
            student.phone_number
        )


@allure.title("fill mobile phone less numbers than required")
def test_fill_mobile_less_than_required(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.gender(student.gender)
    registration_page.type_phone("205555124")

    registration_page.click_submit()

    # THEN
    registration_page.validation_phone()


@allure.title("Fill email on incorrect format")
def test_email_validation(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.gender(student.gender)
    registration_page.type_phone(student.phone_number)
    registration_page.fill_email("test@test")

    registration_page.click_submit()

    # THEN

    registration_page.validation_email()
