import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
print(driver.current_url)
print(driver.title)


#Locators: ID, NAME, CLASS_NAME, TAG_NAME, LINKTEXT, XPATH, CSS_SELECTOR

driver.find_element(By.NAME, "email").send_keys("Shubhangi12@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(2)

driver.find_element(By.ID,"inlineRadio2").click()

# CSS syntax : tagname[attribute = 'value']    , #id , .classname
driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("Shubhangi")

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(2)

#xpath syntax: //tagname [@attribute = 'value ']
driver.find_element(By.XPATH,"//input[@class = 'btn btn-success']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "success" in message

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Hello")
time.sleep(3)
