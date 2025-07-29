import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")
time.sleep(3)
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

#FirstName
driver.find_element(By.ID, "firstName").send_keys("Shubhangi")
#LastName
driver.find_element(By.CSS_SELECTOR , "input[placeholder ='Last Name']").send_keys("Patil")
#EmailID
driver.find_element(By.ID, "userEmail").send_keys("Abcd12@gmail.com")
#Phonenumber
driver.find_element(By.CSS_SELECTOR, "[placeholder ='enter your number']").send_keys(75843903)
#Occuptaion
driver.find_element(By.XPATH, "//option[4]").click()
#Gender: male/female
driver.find_element(By.XPATH, "//input[@value = 'Female']").click()
#password
driver.find_element(By.ID, "userPassword").send_keys("Abcd@123")
#confirm Password
driver.find_element(By.ID, "confirmPassword").send_keys("Abcd@123")
#Select Checkbox
driver.find_element(By.XPATH, "//input[@formcontrolname='required']").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,800)")
#SubmitButton
#driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
#driver.find_element(By.ID,"login").click()

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "login")))
next = driver.find_element(By.ID,"login")
next.click()
time.sleep(3)