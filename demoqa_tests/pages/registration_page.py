import os
from selene import be, have
from selene.support.shared import browser
from demoqa_tests.data.user import User


class RegistrationPage:

    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def filling_registration_form(self, user: User):
        browser.element('#firstName').should(be.blank).type(f'{user.first_name}')
        browser.element('#lastName').type(f'{user.last_name}')
        browser.element('#userEmail').type(f'{user.email}')
        browser.element('.custom-control-label').should(have.text(f'{user.gender}')).click()
        browser.element('#userNumber').type(f'{user.phone}')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{user.year_birth}"]').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{user.month_birth}"]').click()
        browser.element(f'.react-datepicker__day--0{user.day_birth}').click()
        browser.element('#subjectsInput').type(f'{user.first_subject}').press_enter().type(f'{user.second_subject}').press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-2"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'{user.downloaded_pic}'))
        browser.element('#currentAddress').type(f'{user.current_address}').press_enter()
        browser.element('#react-select-3-input').type(f'{user.state}').press_enter()
        browser.element('#react-select-4-input').type(f'{user.city}').press_enter()
        browser.element('#submit').press_enter()

    def should_have_by_registered(self, user: User):
        (browser.element('tbody').all('tr td:nth-child(2)')
         .should(have.texts(f'{user.first_name} {user.last_name}', user.email,
                            user.gender, user.phone, '21 December,2001',
                            'Computer Science, Physics',
                            'Sports, Reading',
                            '1.jpg', f'{user.current_address}',
                            'Haryana Karnal')))