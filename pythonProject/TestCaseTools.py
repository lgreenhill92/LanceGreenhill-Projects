# from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from itertools import zip_longest
import pandas as pd
import numpy as np
import openpyxl
import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell


def return_home(browser):
    elem = browser.find_element(By.CSS_SELECTOR, '.dashboard .icon').click()


def admin_sign_in(self):
    user_name = ''
    user_name_password = ''
    if self == "integration":
        user_name = 'lgreenhill@specmeters.com'
        user_name_password = 'LG210057lg!'
    # return user_name, user_name_password

    # return "You can become a web developer."
    elif self == "development":
        user_name = 'lgreenhill@specmeters.com'
        user_name_password = 'LG210057lg!!622'
    # return user_name, user_name_password

    elif self == "production":
        user_name = 'lgreenhill@specmeters.com'
        user_name_password = 'LG210057lg!'
        # return user_name, user_name_password

    return user_name, user_name_password


def server_choice(self):
    if self == "integration":
        # browser.get('https://int.specconnect.net/tab/dashboard')
        # assert 'SpecConnect' in browser.title
        webpage = 'https://int.specconnect.net/tab/dashboard'
        return webpage
    elif self == "int":
        # browser.get('https://int.specconnect.net/tab/dashboard')
        # assert 'SpecConnect' in browser.title
        webpage = 'https://int.specconnect.net/tab/dashboard'
        return webpage
    elif self == "dev":
        # browser.get('https://dev.specconnect.net/tab/dashboard')
        # assert 'SpecConnect' in browser.title
        webpage = 'https://dev.specconnect.net/tab/dashboard'
        return webpage
    elif self == "development":
        # browser.get('https://dev.specconnect.net/tab/dashboard')
        # assert 'SpecConnect' in browser.title
        webpage = 'https://dev.specconnect.net/tab/dashboard'
        return webpage
    elif self == "production":
        # browser.get('https://www.specconnect.net/tab/dashboard')
        # assert 'SpecConnect' in browser.title
        webpage = 'https://www.specconnect.net/tab/dashboard'
        return webpage


def open_login(server, browser):
    wdriver = server_choice(server)
    browser.get(wdriver)

    assert 'SpecConnect' in browser.title
    browser.set_window_size(1723, 1040)

    elem = browser.find_element(By.ID, 'Email')  # Find the search box
    elem.send_keys(admin_sign_in(server)[0])

    elem = browser.find_element(By.ID, 'Password')  # Find the search box
    elem.send_keys(admin_sign_in(server)[1] + Keys.RETURN)


"""
Finish creating function to insert ie drop elements in 
"""


def excel_file_compare(template_file_location, template_file_name, test_file_location, test_file_name):
    template = pd.read_excel("C:/Local files/Testfolder/AutotestHourlyExportNoedit.xlsx", na_values=np.nan, header=None)
    testSheet = pd.read_excel("C:/Local files/Testfolder/AutotestHourlyExportedited.xlsx", na_values=np.nan,
                              header=None)

    rt, ct = template.shape
    rtest, ctest = testSheet.shape

    df = pd.DataFrame(columns=['Cell_Location', 'BaseTemplate_Value', 'CurrentFile_Value'])
    i = 0
    rowcount = range(max(rt, rtest))
    for rowNo in range(max(rt, rtest)):
        i += 1
        for colNo in range(max(ct, ctest)):
            # Fetching the template value at a cell
            try:
                template_val = template.iloc[rowNo, colNo]
            except:
                template_val = np.nan

            # Fetching the testsheet value at a cell
            try:
                testSheet_val = testSheet.iloc[rowNo, colNo]
            except:
                testSheet_val = np.nan

            # Comparing the values
            if str(template_val) != str(testSheet_val):
                cell = xl_rowcol_to_cell(rowNo, colNo)
                dfTemp = pd.DataFrame([[cell, template_val, testSheet_val]],
                                      columns=['Cell_Location', 'BaseTemplate_Value', 'CurrentFile_Value'])
                df = pd.concat([df, dfTemp], ignore_index=True)
        if df.empty:
            match = True
        elif i == (max(rowcount)):
            print("We may have a data change. Please verify locations")
            dfOut = df.to_string(index=False)
            print(f"{dfOut}\n")
            # print("Hello" + match + "")
            # match = True
        else:
            # print(i)
            # print(max(rowcount))
            # print("Data Error")
            dfOut = df.to_string(index=False)
            # print(f"{dfOut}\n")
            match = False
        # print("\n")


def compare_csv(file1, file2):
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        if df1.equals(df2):
            print("File validation passed.")
            return "Pass"
        else:
            diff_df = df1.compare(df2)
            print("Differences between files:")
            print(diff_df)
            return "Fail"
    except:
        print("A data error occurred.\nThe data file comparision seems to not match my testing."
              "\nVerify that your file location is correct."
              + "\nExample of file path: C:/temp/HourlyExport.csv.\n")


def activity_peak(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Activity Peek').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Activity Peek":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def clear_rainfall(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Clear Rainfall').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Clear Rainfall Data":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def customer_api(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Customer API Keys').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Customer API Keys":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def customer_management(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Customer Management').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Edit Customer":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def deployment_monitor(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Deployment Monitor').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Deployment Monitor":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def disease_model_subscriptions(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Disease Model Subscriptions').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Customer Disease Model Subscriptions":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def distributor_management(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Distributor Management').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Distributors":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def equipment_management(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Equipment Management').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Manage Customer Equipment":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def generate_debug_key(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Generate Debug Key').click()

    elem = browser.find_element(By.CLASS_NAME, 'smallh1')

    # formatted diffrent have to find another way to tie in
    if elem.text == "Generate Temporary Device Command Interface Key":
        # if elem == "Generate Debug Key":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def generate_device_key(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Generate Device Key').click()

    elem = browser.find_element(By.CLASS_NAME, 'smallh1')

    if elem.text == "Generate Temporary Device Key":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def serial_number_search(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Serial Number Search').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Global Search By Serial Number":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def terminal_mode(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'Terminal Mode').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Terminal Mode":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def user_management(browser):
    profile_dropdown = browser.find_element(By.CSS_SELECTOR, '.fa-chevron-down')
    profile_dropdown.click()

    profile_dropdown_admin = browser.find_element(By.LINK_TEXT, 'Administrative')
    # profile_dropdown_admin = browser.find_element(By.CLASS_NAME, 'admin.dropdown-submenu ')

    action = ActionChains(browser)
    action.move_to_element(profile_dropdown_admin).perform()

    elem = browser.find_element(By.LINK_TEXT, 'User Management').click()

    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Users":
        print("Text validation test passed.(this test can be as detailed as needed)")
    else:
        print("Text validation test failed.")


def hourly_report(browser):
    print("\nhourly_report")
    elem = browser.find_element(By.CSS_SELECTOR, '.reports .icon').click()
    elem = browser.find_element(By.LINK_TEXT, 'Hourly Report').click()
    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Hourly Report":
        # in case didnt start on 3600
        # elem = browser.find_element(By.ID, 'CustomerAutoComplete')
        # elem.click()
        # elem.send_keys(Keys.BACKSPACE)
        # elem.send_keys("3600")
        # elem = browser.find_element(By.ID, 'ui-id-12').click()
        today = date.today()

        elem = browser.find_element(By.ID, 'StartDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(2)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .day:nth-child(7)').click()

        elem = browser.find_element(By.ID, 'EndDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(7)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .range:nth-child(3)').click()

        select_element = browser.find_element(By.ID, 'EquipmentSN')
        select = Select(select_element)
        option_list = select.options
        select.select_by_value('270009879')
        # chicago is selected now export and compare

        # elem = browser.find_element(By.ID, 'Export').click()
        # elem = browser.find_element(By.ID, 'DlgFileName').type("SeleniumHourly" + today + "Export.csv")
        # elem = browser.find_element(By.CSS_SELECTOR, '.ui-dialog:nth-child(27) > .ui-dialog-buttonpane .ui-button:nth-child(2)').click()

        # create a wait function on file... it may work in case of slow load times

        # compare_csv("C:/temp/HourlyExport.csv", "C:/temp/HourlyExport2.csv")
        #compare_csv("C:\Local files\home\SeleniumTest\Test Template Folder\Reports Chicago South loop data-2-1-2014-to-7-1-2014", "C:/Users/lgreenhill/Downloads/HourlyExport.csv")
        compare_csv("C:/Users/lgreenhill/Downloads/HourlyExport.csv", "C:/temp/HourlyExport2.csv")  # pass
        #compare_csv("C:/Users/lgreenhill/Downloads/HourlyExport.csv", "C:/temp/HourlyExport4.csv")  #fail
        print("Website validation test passed.(this test can be as detailed as needed)")
    else:
        print("Website validation test failed.\n")

def DLI_report(browser):
    print("\nDLI_report")
    elem = browser.find_element(By.CSS_SELECTOR, '.reports .icon').click()
    elem = browser.find_element(By.LINK_TEXT, 'DLI Report').click()
    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "DLI Report":
        # in case didnt start on 3600
        # elem = browser.find_element(By.ID, 'CustomerAutoComplete')
        # elem.click()
        # elem.send_keys(Keys.BACKSPACE)
        # elem.send_keys("3600")
        # elem = browser.find_element(By.ID, 'ui-id-12').click()
        today = date.today()

        elem = browser.find_element(By.ID, 'StartDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(2)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .day:nth-child(7)').click()

        elem = browser.find_element(By.ID, 'EndDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(7)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .range:nth-child(3)').click()

        select_element = browser.find_element(By.ID, 'SensorId')
        select = Select(select_element)
        option_list = select.options
        select.select_by_value('1092:A:7')
        # chicago is selected now export and compare

        # elem = browser.find_element(By.ID, 'Export').click()
        # elem = browser.find_element(By.ID, 'DlgFileName').type("SeleniumHourly" + today + "Export.csv")
        # elem = browser.find_element(By.CSS_SELECTOR, '.ui-dialog:nth-child(27) > .ui-dialog-buttonpane .ui-button:nth-child(2)').click()

        # create a wait function on file... it may work in case of slow load times

        # compare_csv("C:/temp/HourlyExport.csv", "C:/temp/HourlyExport2.csv")
        #compare_csv("C:\Local files\home\SeleniumTest\Test Template Folder\Reports Chicago South loop data-2-1-2014-to-7-1-2014", "C:/Users/lgreenhill/Downloads/HourlyExport.csv")
        compare_csv("C:/Users/lgreenhill/Downloads/DLIExport.csv", "C:/Users/lgreenhill/iCloudDrive/Work Desktop/Regresssion Test Data Templates/Reports Chicago South loop data-2-1-2014-to-7-1-2014/DLIExport (05_01_2015 - 06_01_2015) south loop (1).csv")  # pass
        #compare_csv("C:/Users/lgreenhill/Downloads/HourlyExport.csv", "C:/temp/HourlyExport4.csv")  #fail
        print("Website validation test passed.(this test can be as detailed as needed)")
    else:
        print("Website validation test failed.\n")

def Daily_Report(browser):
    print("\nDaily_Report")
    elem = browser.find_element(By.CSS_SELECTOR, '.reports .icon').click()
    elem = browser.find_element(By.LINK_TEXT, 'Daily Report').click()
    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Daily Report":
        # in case didnt start on 3600
        # elem = browser.find_element(By.ID, 'CustomerAutoComplete')
        # elem.click()
        # elem.send_keys(Keys.BACKSPACE)
        # elem.send_keys("3600")
        # elem = browser.find_element(By.ID, 'ui-id-12').click()
        today = date.today()

        elem = browser.find_element(By.ID, 'StartDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(2)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .day:nth-child(7)').click()

        elem = browser.find_element(By.ID, 'EndDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(7)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .range:nth-child(3)').click()

        select_element = browser.find_element(By.ID, 'EquipmentSN')
        select = Select(select_element)
        option_list = select.options
        select.select_by_value('270009879')
        # chicago is selected now export and compare

        # elem = browser.find_element(By.ID, 'Export').click()
        # elem = browser.find_element(By.ID, 'DlgFileName').type("SeleniumHourly" + today + "Export.csv")
        # elem = browser.find_element(By.CSS_SELECTOR, '.ui-dialog:nth-child(27) > .ui-dialog-buttonpane .ui-button:nth-child(2)').click()

        # create a wait function on file... it may work in case of slow load times

        # compare_csv("C:/temp/HourlyExport.csv", "C:/temp/HourlyExport2.csv")
        #compare_csv("C:\Local files\home\SeleniumTest\Test Template Folder\Reports Chicago South loop data-2-1-2014-to-7-1-2014", "C:/Users/lgreenhill/Downloads/HourlyExport.csv")
        compare_csv("C:/Users/lgreenhill/Downloads/DLIExport.csv", "C:/Users/lgreenhill/iCloudDrive/Work Desktop/Regresssion Test Data Templates/Reports Chicago South loop data-2-1-2014-to-7-1-2014/DLIExport (05_01_2015 - 06_01_2015) south loop (1).csv")  # pass
        #compare_csv("C:/Users/lgreenhill/Downloads/HourlyExport.csv", "C:/temp/HourlyExport4.csv")  #fail
        print("Website validation test passed.(this test can be as detailed as needed)")
    else:
        print("Website validation test failed.\n")

def Multistation_report(browser):
    print("\nMultistation_report IN PROGRESS")
    elem = browser.find_element(By.CSS_SELECTOR, '.reports .icon').click()
    elem = browser.find_element(By.LINK_TEXT, 'Multi Station/Sensor Report').click()
    elem = browser.find_element(By.CLASS_NAME, 'page-title')

    if elem.text == "Multi Station/Sensor Report":
        # in case didnt start on 3600
        # elem = browser.find_element(By.ID, 'CustomerAutoComplete')
        # elem.click()
        # elem.send_keys(Keys.BACKSPACE)
        # elem.send_keys("3600")
        # elem = browser.find_element(By.ID, 'ui-id-12').click()
        today = date.today()

        elem = browser.find_element(By.ID, 'StartDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(2)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .day:nth-child(7)').click()

        elem = browser.find_element(By.ID, 'EndDate').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-days .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-months .datepicker-switch').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.datepicker-years .prev').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.year:nth-child(6)').click()
        elem = browser.find_element(By.CSS_SELECTOR, '.month:nth-child(7)').click()
        elem = browser.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .range:nth-child(3)').click()

        select_element = browser.find_element(By.ID, 'EquipmentSN')
        select = Select(select_element)
        option_list = select.options
        select.select_by_value('270009879')
        # chicago is selected now export and compare

        # elem = browser.find_element(By.ID, 'Export').click()
        # elem = browser.find_element(By.ID, 'DlgFileName').type("SeleniumHourly" + today + "Export.csv")
        # elem = browser.find_element(By.CSS_SELECTOR, '.ui-dialog:nth-child(27) > .ui-dialog-buttonpane .ui-button:nth-child(2)').click()

        # create a wait function on file... it may work in case of slow load times

        # compare_csv("C:/temp/HourlyExport.csv", "C:/temp/HourlyExport2.csv")
        #compare_csv("C:\Local files\home\SeleniumTest\Test Template Folder\Reports Chicago South loop data-2-1-2014-to-7-1-2014", "C:/Users/lgreenhill/Downloads/HourlyExport.csv")
        compare_csv("C:/Users/lgreenhill/Downloads/DLIExport.csv", "C:/Users/lgreenhill/iCloudDrive/Work Desktop/Regresssion Test Data Templates/Reports Chicago South loop data-2-1-2014-to-7-1-2014/DLIExport (05_01_2015 - 06_01_2015) south loop (1).csv")  # pass
        #compare_csv("C:/Users/lgreenhill/Downloads/HourlyExport.csv", "C:/temp/HourlyExport4.csv")  #fail
        print("Website validation test passed.(this test can be as detailed as needed)")
    else:
        print("Website validation test failed.\n")

def Administrative_tab(browser):
    print("Administrative tab regression test in progress.\n")

    print("activity_peak")
    activity_peak(browser)
    print("\nclear_rainfall")
    clear_rainfall(browser)
    print("\ncustomer_api")
    customer_api(browser)
    print("\ncustomer_management")
    customer_management(browser)
    print("\ndeployment_monitor")
    deployment_monitor(browser)
    print("\ndisease_model")
    disease_model_subscriptions(browser)
    print("\ndistributor_management")
    distributor_management(browser)
    print("\nequipment_management")
    equipment_management(browser)
    print("\ngenerate_debug_key")
    generate_debug_key(browser)
    print("\ngenerate_device_key")
    generate_device_key(browser)
    print("\nserial_number_search")
    serial_number_search(browser)
    print("\nterminal_mode")
    terminal_mode(browser)
    print("\nuser_management")
    user_management(browser)

    return_home(browser)

# class TestCaseTools:
#     def environment(self):
#         new_browser = "webdriver." + self + "()"
#         return new_browser
#         #print(new_browser)
#
#     def admin_sign_in(self):
#         user_name = ''
#         user_name_password = ''
#         if self == "integration":
#             user_name = 'lgreenhill@specmeters.com'
#             user_name_password = 'LG210057lg!'
#            # return user_name, user_name_password
#
#             # return "You can become a web developer."
#         elif self == "development":
#             user_name = 'lgreenhill@specmeters.com'
#             user_name_password = 'LG210057lg!622!'
#            # return user_name, user_name_password
#
#         elif self == "production":
#             user_name = 'lgreenhill@specmeters.com'
#             user_name_password = 'LG210057lg!'
#             #return user_name, user_name_password
#
#         return user_name, user_name_password
#
#     def server_choice(self):
#         if self == "integration":
#             #browser.get('https://int.specconnect.net/tab/dashboard')
#             #assert 'SpecConnect' in browser.title
#             webpage = 'https://int.specconnect.net/tab/dashboard'
#             return webpage
#         elif self == "int":
#             # browser.get('https://int.specconnect.net/tab/dashboard')
#             # assert 'SpecConnect' in browser.title
#             webpage = 'https://int.specconnect.net/tab/dashboard'
#             return webpage
#         elif self == "dev":
#             # browser.get('https://dev.specconnect.net/tab/dashboard')
#             # assert 'SpecConnect' in browser.title
#             webpage = 'https://dev.specconnect.net/tab/dashboard'
#             return webpage
#         elif self == "development":
#             # browser.get('https://dev.specconnect.net/tab/dashboard')
#             # assert 'SpecConnect' in browser.title
#             webpage = 'https://dev.specconnect.net/tab/dashboard'
#             return webpage
#         elif self == "production":
#             # browser.get('https://www.specconnect.net/tab/dashboard')
#             # assert 'SpecConnect' in browser.title
#             webpage = 'https://www.specconnect.net/tab/dashboard'
#             return webpage


# if __name__ == '__main__':
#
#     browser = "Chrome"
#     server = "development"
#
#     print(TestCaseTools.environment(browser))
#     print(TestCaseTools.admin_sign_in(server))
#     print(TestCaseTools.server_choice(server))
