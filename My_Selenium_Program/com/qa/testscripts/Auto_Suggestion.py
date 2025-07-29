import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print(driver.title)

time.sleep(2)

#AutoSuggest Search Functionality

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
Country = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print("Auto_Suggestion Country :")

##enumerate(Country, 1) gives both the index (starting at 1) and the WebElement.
for index, country in enumerate(Country, 1):

##country.text retrieves the visible text of each suggestion.
    print(f"{index}. {country.text}")

print("Total suggestion Count or size :",len(Country))
time.sleep(2)

#autosuggest dropdown
for Coun in Country:
    if Coun.text == "India":
        Coun.click()
        break

#print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
#By using assertion
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"