from demoqa_tests.pages.registration_page import RegistrationPage

reg_page = RegistrationPage()


def test_filling_form():
    reg_page.open_page()

    reg_page.first_name_fill('Roman')
    reg_page.second_name_fill('Bazaleev')
    reg_page.email_fill('bazaleev.roma@ya.ru')
    reg_page.gender_fill('Male')
    reg_page.phone_fill('8800555353')
    reg_page.birth_fill(year=2001, month=10, day=21)
    reg_page.subjects_fill('computer science', 'physics')
    reg_page.hobbies_fill(sports='sports', reading='reading')
    reg_page.download_pic(file_name='1.jpg')
    reg_page.current_address_fill('Pushkina Kolotushkina 1337')
    reg_page.state_fill('haryana')
    reg_page.city_fill('karnal')
    reg_page.submit()

    reg_page.should_have_words('Roman Bazaleev', 'bazaleev.roma@ya.ru',
                               'Male', '8800555353', 'Computer Science, Physics',
                               '21 November,2001', '1.jpg', 'Pushkina Kolotushkina 1337',
                               'Haryana Karnal', 'Sports, Reading')
