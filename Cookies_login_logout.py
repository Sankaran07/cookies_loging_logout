from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get("https://www.saucedemo.com/")

# Function to display cookies
def display_cookies():
    cookies = driver.get_cookies()
    print("Cookies:")
    for cookie in cookies:
        print(cookie)
sleep(1)
# Before login
print("Before Login:")
display_cookies()

# Login
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
sleep(1)

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Wait until login is successful and redirect to the inventory page
WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
sleep(1)

# After login
print("\nAfter Login:")
display_cookies()
sleep(1)


setting_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
setting_button.click()

# Logout
logout_button = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
logout_button.click()


# Verify logout
WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/"))
sleep(1)

# After logout
print("\nAfter Logout:")
display_cookies()

# Close the WebDriver session
driver.quit()
