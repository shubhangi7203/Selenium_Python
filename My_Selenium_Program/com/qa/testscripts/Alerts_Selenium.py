from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# -------------------------------
# 1️⃣ SIMPLE ALERT (Only OK)
# -------------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
simple_alert = driver.switch_to.alert
print("Simple Alert Text:", simple_alert.text)
time.sleep(2)
simple_alert.accept()  # Click OK
time.sleep(2)

# -------------------------------
# 2️⃣ CONFIRMATION ALERT (OK / Cancel)
# -------------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm_alert = driver.switch_to.alert
print("Confirmation Alert Text:", confirm_alert.text)
time.sleep(2)
confirm_alert.dismiss()  # Click Cancel (can also use .accept())
time.sleep(2)

# -------------------------------
# 3️⃣ PROMPT ALERT (Input + OK / Cancel)
# -------------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt_alert = driver.switch_to.alert
print("Prompt Alert Text:", prompt_alert.text)
prompt_alert.send_keys("Selenium Test")  # Enter text into prompt
time.sleep(2)
prompt_alert.accept()  # Click OK
time.sleep(2)

# -------------------------------
# Close browser
driver.quit()
