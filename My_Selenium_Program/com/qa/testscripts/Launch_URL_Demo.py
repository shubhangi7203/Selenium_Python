import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

##-->is a shortcut to launch Microsoft Edge without explicitly specifying the path to the WebDriver executable.
driver = webdriver.Edge()


## Creates a Service object that points to the exact location of your msedgedriver.exe.
##-->✅ This object is required by Selenium to start a new Edge browser session.
##-->📌 Double backslashes \\ are used in the file path because \ is an escape character in Python.

    #service_obj = Service("C:\\Users\\SS\\Downloads\\edgedriver_win64 (2)\\msedgedriver.exe")
    #driver = webdriver.Edge(service=service_obj)

##-->🔹 Navigates the browser to the URL — in this case, the Ferns N Petals homepage.
driver.get("https://www.fnp.com/")

##-->🔹 Maximizes the browser window to full screen.
driver.maximize_window()

##-->🔹 Retrieves and prints the title of the currently loaded page.
print("Title of the Page : "+driver.title)

##-->🔹 Retrieves and prints the current URL loaded in the browser — useful for validation.
print("Current URL of the Page :"+driver.current_url)

##-->🔹 Pauses the script for 2 seconds so that the browser window remains open briefly.
time.sleep(2)


