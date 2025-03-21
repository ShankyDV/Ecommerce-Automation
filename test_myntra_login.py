from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Edge WebDriver
driver = webdriver.Edge()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Setup Explicit Wait
wait = WebDriverWait(driver, 60)

try:
    # Click on "Login"
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
    login_button.click()

    # Enter Phone Number
    phone_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div/form/div[1]/input")))
    phone_input.clear()
    phone_input.send_keys("7834961234")  # Use a valid phone number

    # Click "Request OTP" Button
    otp_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div/form/div[3]/button")))
    otp_button.click()

    # Wait for User to Enter OTP
    print("⏳ Waiting for user to enter OTP manually...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Verify')]")))  # Adjust if needed
    print("✅ OTP entered! Proceeding further...")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
