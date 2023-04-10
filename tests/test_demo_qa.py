import allure
from selene.support.shared import browser
from demo_qa_lesson5 import registration_form
from users.users import User, Subjects, Hobbies
from utils import attach


student = User(
    first_name='Uladzislau',
    last_name="Makhakhei",
    email='vladqaguru@gmail.com',
    day_of_birth='03',
    month_of_birth='July',
    year_of_birth='1994',
    gender='Male',
    phone_number='2055551215',
    subjects=[Subjects.maths.value, Subjects.biology.value],
    hobbies=[Hobbies.Music.value, Hobbies.Sports.value],
    name_picture='picture.jpg',
    adress='Minsk',
    state='NCR',
    city='Noida',
)


@allure.title('Register user')
def test_fill_fields(setup_browser):

    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.register(student)
    registration_page.click_submit()
    # THEN
    registration_page.assert_registred_user(student)

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
