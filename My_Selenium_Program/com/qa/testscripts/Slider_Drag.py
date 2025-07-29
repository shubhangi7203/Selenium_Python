from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open Flipkart mobile phones store page
driver.get("https://www.flipkart.com/mobile-phones-store")

# Step 3: Wait for the page to load fully
time.sleep(5)

# Step 5: Scroll down to bring slider into view
driver.execute_script("window.scrollBy(0, 200)")

# Step 6: Locate the left (min) and right (max) slider handles
min_slider = driver.find_element(By.XPATH, "(//div[@class='PYKUdo'])[1]")
max_slider = driver.find_element(By.XPATH, "(//div[@class='PYKUdo'])[2]")

# Step 7: Use ActionChains to drag sliders
actions = ActionChains(driver)

# Example: Move left (min) slider to right by 50 pixels
#actions.click_and_hold(min_slider).move_by_offset(50, 0).release().perform()
time.sleep(2)

# Example: Move right (max) slider to left by 50 pixels
actions.click_and_hold(max_slider).move_by_offset(-70, 0).release().perform()
time.sleep(2)

# Step 8: Optional - Close browser
driver.quit()
