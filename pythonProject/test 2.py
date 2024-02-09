#from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class GoogleTestCase(unittest.TestCase):

    browser = webdriver.Chrome()

    browser.get('https://dev.specconnect.net/tab/dashboard')
    assert 'SpecConnect' in browser.title
    # elem.send_keys('lgreenhill@specmeters.com' + Keys.RETURN)

    elem = browser.find_element(By.ID, 'Email')  # Find the search box
    elem.send_keys('lgreenhill@specmeters.com')

    elem = browser.find_element(By.ID, 'Password')  # Find the search box
    elem.send_keys('LG210057lg!!622' + Keys.RETURN)

    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    #profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Activity Peek').click()

#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

