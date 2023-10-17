import os

from selene import be, have
from selene.support.shared import browser


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

    def birth_fill(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="2001"]').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
        browser.element('.react-datepicker__day--021').click()

    def subjects_fill(self, first_subj, second_subj):
        return browser.element('#subjectsInput').type(f'{first_subj}').press_enter().type(f'{second_subj}').press_enter()

    def hobbies_fill(self):
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-2"]').click()

    def download_pic(self, path_to_file):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'{path_to_file}'))

    def current_address_fill(self, address):
        browser.element('#currentAddress').type(f'{address}').press_enter()

    def state_fill(self, state):
        browser.element('#react-select-3-input').type(f'{state}').press_enter()

    def city_fill(self, city):
        browser.element('#react-select-4-input').type(f'{city}').press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_have_words(self):
        (browser.element('tbody').all('tr td:nth-child(2)')
         .should(have.texts('Roman Bazaleev', 'bazaleev.roma@ya.ru',
                                                                             'Male', '8005553535', '21 November,2001',
                                                                             'Computer Science, Physics',
                                                                             'Sports, Reading',
                                                                             '1.jpg', 'Pushkina Kolotushkina 1337',
                                                                             'Haryana Karnal')))


