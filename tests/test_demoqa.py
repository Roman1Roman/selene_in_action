import os
from model.registration_page import RegistrationPage
from selene import browser, be, have


reg_page = RegistrationPage()

def test_filling_form():
    reg_page.open_page()

    reg_page.first_name_fill('Roman')
    reg_page.second_name_fill('Bazaleev')
    reg_page.email_fill('bazaleev.roma@ya.ru')
    reg_page.gender_fill('Male')
    reg_page.phone_fill('8005553535')
    reg_page.birth_fill()
    reg_page.subjects_fill('co', 'ph')
    reg_page.hobbies_fill()
    reg_page.download_pic('files/1.jpg')
    reg_page.current_address_fill('Pushkina Kolotushkina 1337')
    reg_page.state_fill('har')
    reg_page.city_fill('karn')
    reg_page.submit()

    reg_page.should_have_words()
