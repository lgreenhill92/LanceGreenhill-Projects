#from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest
import TestCaseTools


class reportsTestCase(unittest.TestCase):

    server = "production"
    browser = webdriver.Chrome()

    TestCaseTools.open_login(server, browser)

    #TestCaseTools.Administrative_tab(browser)

    TestCaseTools.hourly_report(browser)
#verify hourly report then create GUI