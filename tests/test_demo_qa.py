from demo_qa_lesson5 import registration_form


def test_fill_fields(browser_setup):
    registration_page = registration_form.RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.fill_first_name('Uladzislau')
    registration_page.fill_last_name('Makhakhei')
    registration_page.fill_email('vladqaguru@gmail.com')
    registration_page.fill_date_of_birth('03', 'July', '1994')
    registration_page.gender('Male')
    registration_page.type_phone('2055551215')
    registration_page.select_subjects('Maths')
    registration_page.select_hobbies('Music')
    registration_page.upload_picture()
    registration_page.fill_current_address('Minsk')
    registration_page.select_state('NCR')
    registration_page.select_city('Noida')

    registration_page.click_submit()

    # THEN
    registration_page.assert_registred_user_info(
        'Uladzislau Makhakhei',
        'vladqaguru@gmail.com',
        'Male',
        '2055551215',
        '03 July,1994',
        'Maths',
        'Music',
        'picture.jpg',
        'Minsk',
        'NCR Noida'
    )
