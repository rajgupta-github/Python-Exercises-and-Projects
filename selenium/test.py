from selenium.webdriver import *
import os

driver = Chrome(executable_path=os.getcwd() + "/chromedriver")
driver.get("https://www.google.com")
driver.maximize_window()
driver.close()