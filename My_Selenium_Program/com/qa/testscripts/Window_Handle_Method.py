from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1️⃣: Launch browser and open URL
driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/popup.php")
driver.maximize_window()
print("🔵 Main window opened")

# Step 2️⃣: Click the link that opens a new window
driver.find_element(By.LINK_TEXT, "Click Here").click()
print("🟢 New window triggered")

# Step 3️⃣: Get window handles
main_window = driver.current_window_handle
all_windows = driver.window_handles
print("🔍 Window Handles:", all_windows)

# Step 4️⃣: Switch to the new window
for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        print("➡️ Switched to new window")

# Step 5️⃣: Perform actions in the new window
driver.find_element(By.NAME, "emailid").send_keys("test@example.com")
driver.find_element(By.NAME, "btnLogin").click()
print("✅ Email entered and login clicked in new window")

# Optional: Wait to see result
time.sleep(2)

# Step 6️⃣: Close the new window and switch back to main window
driver.close()
print("❌ Closed new window")

driver.switch_to.window(main_window)
print("↩️ Switched back to main window")

# Step 7️⃣: Do something else in main window (if needed)
print("🔚 Window handling completed")

# Step 8️⃣: Quit browser
driver.quit()
