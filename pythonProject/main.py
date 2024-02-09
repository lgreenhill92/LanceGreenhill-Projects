#from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import TestCaseTools


class Regression_test_cycle_RevXX(unittest.TestCase):
    #GUI.root.mainloop()
    server = "integration"
    browser = webdriver.Chrome()
    TestCaseTools.open_login(server, browser)

    #TestCaseTools.Administrative_tab(browser)
    TestCaseTools.hourly_report(browser)
    TestCaseTools.DLI_report(browser)
    TestCaseTools.Daily_Report(browser)
    TestCaseTools.return_home(browser)
