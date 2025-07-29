import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
print(driver.title)

driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("learning")
time.sleep(2)

#Static DropDown:
#There are 3 methods 1.select_By_visible_text, 2.Select_By_index, 3. Select_By_value

dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
#dropdown.select_by_index(2)
#dropdown.select_by_visible_text("Consultant")
dropdown.select_by_value("consult")
time.sleep(3)

driver.find_element(By.ID, "terms").click()
time.sleep(2)

driver.find_element(By.ID, "signInBtn").click()
time.sleep(3)

