from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
driver.maximize_window()
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Navigate to YouTube
driver.get("https://www.youtube.com")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Go Back to Google
driver.back()
print("Back → Title:", driver.title)
time.sleep(2)

# Go Forward to YouTube
driver.forward()
print("Forward → Title:", driver.title)
time.sleep(2)

# Refresh YouTube
driver.refresh()
print("Refreshed → Title:", driver.title)
time.sleep(2)

# Close Browser
driver.quit()

