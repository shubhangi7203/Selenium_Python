from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open drag-and-drop demo page
driver.get("https://jqueryui.com/droppable/")

# Switch to the frame that contains the draggable and droppable elements
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Identify the source and target elements
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# Perform drag and drop using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

# Wait to see result
time.sleep(3)
driver.quit()
