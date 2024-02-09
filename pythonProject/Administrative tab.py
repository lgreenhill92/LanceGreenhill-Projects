#from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import TestCaseTools
import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Python rocks!")
label.pack()

window.mainloop()









#class GoogleTestCase(unittest.TestCase):




#     server = "production"
#     browser = webdriver.Chrome()
#
#     TestCaseTools.open_login(server, browser)
#
#     TestCaseTools.activity_peak(browser)
#
#     TestCaseTools.return_home(browser)
#
#
#
#
#
#
#
#
#
#
# # if __name__ == '__main__':
# #     unittest.main(verbosity=2)
# #     browser = "Chrome"
# #     server = "development"
#
#
#
#
#
#     # TestCaseTools.webdriver(browser)
#     # print(TestCaseTools.admin_sign_in(server))
#     # print(TestCaseTools.server_choice(server))
#
