from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(2)

# 1️⃣ Switch to frame using **index**
driver.find_element(By.XPATH, "//a[contains(text(),'Single Iframe')]").click()
time.sleep(2)
driver.switch_to.frame(0)
input_box = driver.find_element(By.XPATH, "//input[@type='text']")
input_box.send_keys("✅ Frame by Index")
time.sleep(2)
driver.switch_to.default_content()
print("🔁 Switched back to default content from index")

# 2️⃣ Switch to frame using **WebElement**
iframe_element = driver.find_element(By.XPATH, "//iframe[@id='singleframe']")
driver.switch_to.frame(iframe_element)
input_box = driver.find_element(By.XPATH, "//input[@type='text']")
input_box.clear()
input_box.send_keys("✅ Frame by WebElement")
time.sleep(2)
driver.switch_to.default_content()
print("🔁 Switched back to default content from WebElement")

# 3️⃣ Switch to **Nested Frames** using **frame by name/id**
driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
time.sleep(2)

# Switch to outer frame
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

# Switch to inner frame (index 0 inside outer)
driver.switch_to.frame(0)

input_nested = driver.find_element(By.XPATH, "//input[@type='text']")
input_nested.send_keys("✅ Nested Frame by index inside WebElement")
time.sleep(2)

# Switch back to default content
driver.switch_to.default_content()
print("🔁 Switched back to default content from nested frame")

# Cleanup
time.sleep(2)
driver.quit()
