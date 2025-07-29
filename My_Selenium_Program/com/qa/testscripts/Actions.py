from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# 1. Hover Over an Element
# -------------------------------
driver.get("https://jqueryui.com/menu/")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
hover_element = driver.find_element(By.ID, "ui-id-2")  # Music
ActionChains(driver).move_to_element(hover_element).perform()
print("User is successfully move to element")
time.sleep(2)

driver.switch_to.default_content()

# -------------------------------
# 2. Double Click
# -------------------------------
driver.get("https://api.jquery.com/dblclick/")
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
double_click_element = driver.find_element(By.TAG_NAME, "div")
ActionChains(driver).double_click(double_click_element).perform()
print("User is successfully double click")
time.sleep(2)

driver.switch_to.default_content()

# -------------------------------
# 3. Right Click (Context Click)
# -------------------------------
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
right_click_element = driver.find_element(By.CSS_SELECTOR, "span.context-menu-one")
ActionChains(driver).context_click(right_click_element).perform()
print("User is successfully Right click")
time.sleep(2)

# -------------------------------
# 4. Drag and Drop
# -------------------------------
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(source, target).perform()
print("User is successfully drag and drop")
time.sleep(2)

driver.switch_to.default_content()

# -------------------------------
# 5. Keyboard Actions (CTRL+A)
# -------------------------------
driver.get("https://www.google.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium with Python")
ActionChains(driver).click(search_box).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
print("User is successfully keyboard Actions")
time.sleep(2)

# Close the browser
driver.quit()
