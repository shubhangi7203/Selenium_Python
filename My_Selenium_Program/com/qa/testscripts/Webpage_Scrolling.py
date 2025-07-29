from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch the browser
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# 1️⃣ Scroll by Pixel
driver.execute_script("window.scrollBy(0, 500);")
print("✅ Scrolled by 500 pixels")
time.sleep(2)

# 2️⃣ Scroll to Bottom of Page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("✅ Scrolled to bottom of page")
time.sleep(2)

# 3️⃣ Scroll to Top of Page
driver.execute_script("window.scrollTo(0, 0);")
print("✅ Scrolled to top of page")
time.sleep(2)

# 4️⃣ Scroll to Element using scrollIntoView
element = driver.find_element(By.ID, "mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
print("✅ Scrolled to element using scrollIntoView")
time.sleep(2)

# 5️⃣ Scroll using ActionChains (move to element)
actions = ActionChains(driver)
actions.move_to_element(element).perform()
print("✅ Scrolled to element using ActionChains")
time.sleep(2)


# Close the browser
driver.quit()
