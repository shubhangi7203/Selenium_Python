from selenium import webdriver
import time

# 1️⃣ Launch Chrome
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://www.google.com")
chrome_driver.maximize_window()
print("Chrome Title:", chrome_driver.title)

# 2️⃣ Launch Firefox
firefox_driver = webdriver.Firefox()
firefox_driver.get("https://www.fnp.com/")
firefox_driver.maximize_window()
print("Firefox Title:", firefox_driver.title)

# 3️⃣ Launch Edge
edge_driver = webdriver.Edge()
edge_driver.get("https://www.igp.com/")
edge_driver.maximize_window()
print("Edge Title:", edge_driver.title)

# 🔄 Pause to view browsers
time.sleep(5)

# ❌ Close All Browsers
chrome_driver.quit()
firefox_driver.quit()
edge_driver.quit()
