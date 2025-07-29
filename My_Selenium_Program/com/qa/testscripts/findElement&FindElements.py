import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.igp.com/")

driver.maximize_window()
print(driver.current_url)
print(driver.title)

SearchTextField = driver.find_element(By.NAME,"q")
SearchTextField.send_keys("cakes")
time.sleep(2)

Suggestion = driver.find_elements(By.XPATH, "//li[@class='cards-li']")
print("Total suggestion :", len(Suggestion))
for Suggest in Suggestion:
    print(Suggest.text)
time.sleep(2)