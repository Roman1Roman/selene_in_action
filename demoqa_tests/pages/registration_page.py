import os

from selene import be, have
from selene.support.shared import browser
from demoqa_tests.resource import path_file

class RegistrationPage:

    def open_page(self):
        return browser.open('/automation-practice-form')

    def first_name_fill(self, name):
        return browser.element('#firstName').should(be.blank).type(f'{name}')

    def second_name_fill(self, surname):
        return browser.element('#lastName').type(f'{surname}')

    def email_fill(self, email):
        return browser.element('#userEmail').type(f'{email}')

    def gender_fill(self, gender):
        return browser.element('.custom-control-label').should(have.text(f'{gender}')).click()

    def phone_fill(self, phone):
        return browser.element('#userNumber').type(f'{phone}')

    def birth_fill(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def subjects_fill(self, first_subj, second_subj):
        return browser.element('#subjectsInput').type(f'{first_subj}').press_enter().type(
            f'{second_subj}').press_enter()

    def hobbies_fill(self, sports, music=None, reading=None):
        if sports == 'sports':
            browser.element('label[for="hobbies-checkbox-1"]').click()
        if music == 'music':
            browser.element('label[for="hobbies-checkbox-3"]').click()
        if reading == 'reading':
            browser.element('label[for="hobbies-checkbox-2"]').click()

    def download_pic(self, file_name):
        browser.element('#uploadPicture').set_value(path_file(file_name))

    def current_address_fill(self, address):
        browser.element('#currentAddress').type(f'{address}').press_enter()

    def state_fill(self, state):
        browser.element('#react-select-3-input').type(f'{state}').press_enter()

    def city_fill(self, city):
        browser.element('#react-select-4-input').type(f'{city}').press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_have_words(self, full_name, email, gender, phone, subjects, birth_date, file_name, address, state_city, hobbies):
        (browser.element('tbody').all('tr td:nth-child(2)')
         .should(have.texts(full_name, email,
                            gender, phone, birth_date,
                            subjects,
                            hobbies,
                            file_name,
                            address,
                            state_city)))
