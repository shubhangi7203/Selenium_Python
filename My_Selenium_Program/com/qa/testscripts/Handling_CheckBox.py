from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()  # Optional: Maximize for better visibility

# Step 2: Open the sample web page with checkboxes
driver.get("https://demo.automationtesting.in/Register.html")

# Step 3: Locate the checkboxes using XPath
checkbox_cricket = driver.find_element(By.XPATH, "//input[@id='checkbox1']")
checkbox_movies = driver.find_element(By.XPATH, "//input[@id='checkbox2']")
checkbox_hockey = driver.find_element(By.XPATH, "//input[@id='checkbox3']")

# Step 4: Check Cricket and Hockey checkboxes if not already selected
if not checkbox_cricket.is_selected():
    checkbox_cricket.click()  # select Cricket checkbox
    time.sleep(2)
    print("✅ 'Cricket' checkbox selected.")
else:
    print("ℹ️ 'Cricket' checkbox was already selected.")

if not checkbox_hockey.is_selected():
    checkbox_hockey.click()  # select Hockey checkbox
    time.sleep(2)
    print("✅ 'Hockey' checkbox selected.")
else:
    print("ℹ️ 'Hockey' checkbox was already selected.")

# Step 5: Uncheck Movies checkbox if it is selected
if checkbox_movies.is_selected():
    checkbox_movies.click()  # deselect Movies checkbox
    time.sleep(2)
    print("🧹 'Movies' checkbox deselected.")
else:
    print("ℹ️ 'Movies' checkbox was already deselected.")

# Step 6: Pause for 2 seconds to observe
time.sleep(2)

# Step 7: Close the browser
driver.quit()
