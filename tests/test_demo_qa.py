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
    with allure.step("Open page"):
        registration_page.open("https://demoqa.com/automation-practice-form")
    with allure.step("Fill all fields valid data"):
        registration_page.register(student)
    with allure.step("Click to submit"):
        registration_page.click_submit()
    # THEN
    with allure.step("Assert entered information"):
        registration_page.assert_registred_user(student)


@allure.title("Submit Empty Form")
def test_submit_empty_form(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    with allure.step("Open page"):
        registration_page.open("https://demoqa.com/automation-practice-form")
    with allure.step("Click to submit"):
        registration_page.click_submit()

    # THEN
    with allure.step("Assert entered Last Name"):
        registration_page.validation_last_name()
    with allure.step("Assert entered First Name"):
        registration_page.validation_first_name()
    with allure.step("Assert entered Gender"):
        registration_page.validation_gender()
    with allure.step("Assert entered Phone number"):
        registration_page.validation_phone()


@allure.title("Fill Only required fields")
def test_fill_required_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()

    with allure.step("Open the page"):
        registration_page.open("https://demoqa.com/automation-practice-form")
    with allure.step("Type the First Name"):
        registration_page.fill_first_name(student.first_name)
    with allure.step("Type the Last Name"):
        registration_page.fill_last_name(student.last_name)
    with allure.step("Select Gender"):
        registration_page.gender(student.gender)
    with allure.step("Tipe the phone number"):
        registration_page.type_phone(student.phone_number)

    with allure.step("Click to submit"):
        registration_page.click_submit()

    # THEN
    with allure.step("Check registered data"):
        registration_page.check_registred_data(student.first_name).check_registred_data(
            student.last_name
        ).check_registred_data(student.gender).check_registred_data(
            student.phone_number
        )


@allure.title("fill mobile phone less numbers than required")
def test_fill_mobile_less_than_required(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    with allure.step("Open browser"):
        registration_page.open("https://demoqa.com/automation-practice-form")
    with allure.step("Fill first name"):
        registration_page.fill_first_name(student.first_name)
    with allure.step("Fill last name"):
        registration_page.fill_last_name(student.last_name)
    with allure.step("Select gender"):
        registration_page.gender(student.gender)
    with allure.step("Type phone number"):
        registration_page.type_phone("205555124")

    with allure.step("Click to submit"):
        registration_page.click_submit()

    # THEN
    with allure.step("Check validate error"):
        registration_page.validation_phone()


@allure.title("Fill email on incorrect format")
def test_email_validation(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    with allure.step("Open the page"):
        registration_page.open("https://demoqa.com/automation-practice-form")
    with allure.step("Fill First Name"):
        registration_page.fill_first_name(student.first_name)
    with allure.step("Fill Last Name"):
        registration_page.fill_last_name(student.last_name)
    with allure.step("Select gender"):
        registration_page.gender(student.gender)
    with allure.step("Fill phone number"):
        registration_page.type_phone(student.phone_number)
    with allure.step("Fill email on incorrect format"):
        registration_page.fill_email("test@test")

    with allure.step("Click tp submit"):
        registration_page.click_submit()

    # THEN
    with allure.step("Assert email validation error"):
        registration_page.validation_email()
