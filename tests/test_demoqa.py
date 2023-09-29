import os
from selene import browser, be, have

def test_filling_form():


    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Roman')
    browser.element('#lastName').type('Bazaleev')
    browser.element('#userEmail').type('bazaleev.roma@ya.ru')
    browser.element('.custom-control-label').should(have.text('Male')).click()
    browser.element('#userNumber').type('8005553535')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="2001"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
    browser.element('.react-datepicker__day--021').click()
    browser.element('#subjectsInput').type('co').press_enter().type('ph').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('files/1.jpg'))
    browser.element('#currentAddress').type('Pushkina Kolotushkina 1337').press_enter()
    browser.element('#react-select-3-input').type('har').press_enter()
    browser.element('#react-select-4-input').type('karn').press_enter()
    browser.element('#submit').press_enter()
    browser.element('tbody').all('tr td:nth-child(2)').should(have.texts('Roman Bazaleev', 'bazaleev.roma@ya.ru',
                                                 'Male', '8005553535', '21 November,2001',
                                                 'Computer Science, Physics', 'Sports, Reading',
                                                 '1.jpg', 'Pushkina Kolotushkina 1337', 'Haryana Karnal'))







    #browser.all("#tod-list>li").should(have.size(3))