import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 🔸 Step 1: Launch browser
driver = webdriver.Chrome()

# 🔸 Step 2: Set Implicit Wait (applies globally)
driver.implicitly_wait(5)

# 🔸 Step 3: Open the application
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()

print("Title:", driver.title)
print("Current URL:", driver.current_url)

# 🔸 Step 4: Use Explicit Wait for Register link
explicit_wait = WebDriverWait(driver, 10)
register_link = explicit_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
register_link.click()

# 🔸 Step 5: Fill form using implicit wait
driver.find_element(By.ID, "firstName").send_keys("Shubhangi")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys("Patil")
driver.find_element(By.ID, "userEmail").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "[placeholder='enter your number']").send_keys("1234567890")
driver.find_element(By.XPATH, "//option[4]").click()
driver.find_element(By.XPATH, "//input[@value='Female']").click()
driver.find_element(By.ID, "userPassword").send_keys("Test@123")
driver.find_element(By.ID, "confirmPassword").send_keys("Test@123")
driver.find_element(By.XPATH, "//input[@formcontrolname='required']").click()

# 🔸 Step 6: Scroll down
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(5)

# 🔸 Step 7: Fluent Wait for Login Button (after registration)
fluent_wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

login_button = fluent_wait.until(EC.element_to_be_clickable((By.ID, "login")))
login_button.click()

# 🔸 Done
print("Login button clicked successfully.")

time.sleep(3)
driver.quit()
