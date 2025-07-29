from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Launch Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open the sample registration page with radio buttons
driver.get("https://demo.automationtesting.in/Register.html")

# Step 3: Wait until the radio buttons are available
wait = WebDriverWait(driver, 10)

# Step 4: Locate radio buttons using XPath
male_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Male']")))
female_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='FeMale']")))

# Step 5: Click on Male radio button if not already selected
if not male_radio.is_selected():
    male_radio.click()
    print("✅ 'Male' radio button selected.")
else:
    print("ℹ️ 'Male' radio button already selected.")

# Step 6: Now click on Female radio button (radio button selection switches)
if not female_radio.is_selected():
    #female_radio.click()
    print("✅ 'Female' radio button selected.")
else:
    print("ℹ️ 'Female' radio button already selected.")

# Optional: Validate final state
if male_radio.is_selected():
    print("👉 Currently selected: Male")
elif female_radio.is_selected():
    print("👉 Currently selected: Female")

# Optional: Wait to observe result
time.sleep(2)

# Step 7: Close browser
driver.quit()
