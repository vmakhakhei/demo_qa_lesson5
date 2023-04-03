from demo_qa_lesson5 import registration_form
from users.users import User, Subjects, Hobby

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
    hobbies=[Hobby.Music.value, Hobby.Sports.value],
    name_picture='picture.jpg',
    adress='Minsk',
    state='NCR',
    city='Noida',
)


def test_fill_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.register(student)
    registration_page.click_submit()
    # THEN
    registration_page.assert_registred_user(student)
