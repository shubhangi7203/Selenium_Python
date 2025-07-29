from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")  # Example site

driver.maximize_window()
print(driver.title)

# Locate the drop-down element
dropdown_element = driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency")

# Create Select object
select = Select(dropdown_element)

# ✅ Select by visible text
select.select_by_visible_text("USD")

# ✅ Select by index (0-based)
select.select_by_index(2)

# ✅ Select by value attribute
select.select_by_value("INR")

# ✅ Get selected option
selected_option = select.first_selected_option
print("Currently selected:", selected_option.text)

time.sleep(3)
driver.quit()
