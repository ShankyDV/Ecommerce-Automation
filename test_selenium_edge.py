from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Edge WebDriver
driver = webdriver.Edge()

# Open an e-commerce website (Amazon as an example)
driver.get("https://www.amazon.in")

# Wait for 3 seconds to load the page
time.sleep(3)

# Print the page title
print("Page title:", driver.title)

# Close the browser
driver.quit()
