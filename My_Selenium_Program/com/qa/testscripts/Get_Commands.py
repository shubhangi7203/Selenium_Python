import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

##-->🔹 Navigates the browser to the URL — in this case, the Ferns N Petals homepage.
driver.get("https://www.fnp.com/")

driver.maximize_window()


##-->🔹 Retrieves and prints the title of the currently loaded page.(# Get page title)
print("Title of the Page : "+driver.title)

##-->🔹 Retrieves and prints the current URL loaded in the browser — useful for validation.(# Get current URL)
print("Current URL of the Page :"+driver.current_url)

##--> Gets the full HTML source code of the page
print("Get source of the page :"+driver.page_source)

##-->	Gets all cookies from the current page
print("Cookies of current page:", driver.get_cookies())

#NO_Thanks = driver.find_element(By.XPATH, "//button[@class='No thanks']")
#print("Button :", NO_Thanks)

time.sleep(2)


