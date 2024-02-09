import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import showinfo

#from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import TestCaseTools

def start_test():
    user_browser = 'webdriver.' + browser.get() + '()'
    user_server = server.get()
    #TestCaseTools.open_login(user_server, user_browser)
    user_testcases = [testcases.get(i) for i in testcases.curselection()]
    for item in user_testcases:
        tool_use = 'TestCaseTools.' + item
        print(user_server, user_browser, item)
        #print(tool_use + user_server, user_browser)



def stop_test():
    # Define your stop test function here
    print("Stop Testing")


# Create main window
root = tk.Tk()
root.geometry('600x250')
root.title('Regression Automation')

# Create Browser combobox
browser_label = ttk.Label(root, text="Browser")
browser_label.grid(column=0, row=0)
browser = ttk.Combobox(root, values=["Chrome", "Internet Explorer"])
browser.grid(column=1, row=0)

# Create Server combobox
server_label = ttk.Label(root, text="Server")
server_label.grid(column=0, row=1)
server = ttk.Combobox(root, values=["Production", "Integration", "Development"])
server.grid(column=1, row=1)

# Create Test Cases listbox with multiple selection
testcases_label = ttk.Label(root, text="Test Cases")
testcases_label.grid(column=0, row=2)
testcases = tk.Listbox(root, selectmode='multiple')
testcases.insert(1, "Administrative_tab")
testcases.insert(2, "Hourly_report")
testcases.insert(3, "Test Case 3")
#user_testcases = tk.ut(value = testcases)
testcases.grid(column=1, row=2)

def testcases_selected(event):
    # get all selected indices
    selected_indices = testcases.curselection()
    # get selected items
    selected_tests = ",".join([testcases.get(i) for i in selected_indices])
    msg = f'You selected: {selected_tests}'
    print(selected_tests)
    # showinfo(title='Information', message=msg)
    #return selected_tests


    #print(selected_indices)

#maybe be able to comment this out
testcases.bind('<<ListboxSelect>>', testcases_selected)


# Create Results scrolled text box
results_label = ttk.Label(root, text="Results")
results_label.grid(column=3, row=1)
results = scrolledtext.ScrolledText(root, width=40, height=10)
results.grid(column=3, row=2)

# Create Start Test button
start_button = ttk.Button(root, text="Start Test", command=start_test)
start_button.grid(column=0, row=4)
#start_button.config(background = 'green')

# Create Stop Test button
stop_button = ttk.Button(root, text="Stop Test", command=stop_test)
stop_button.grid(column=1, row=4)
#stop_button.config(background='red')

root.mainloop()
