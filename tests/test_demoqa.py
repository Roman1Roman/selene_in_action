from demoqa_tests.data.user import User
from demoqa_tests.pages.registration_page import RegistrationPage

def test_registration_form():
     student = User(first_name="Roman", last_name="Bazaleev", email="bazaleev.roma@ya.ru", gender="Male",
                    first_subject='co', second_subject='ph', phone='8800555353', city="karn", state="har",
                    current_address='Pushkina Kolotushkina 228', day_birth='21', month_birth='11', year_birth='2001',
                    downloaded_pic='files/1.jpg')
     rp = RegistrationPage()


     rp.open_page()

     rp.filling_registration_form(user=student)

     rp.should_have_by_registered(user=student)
