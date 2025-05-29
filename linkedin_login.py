from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

EMAIL = "your_email"
PASSWORD = "your_password"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.linkedin.com/login")

   
    wait = WebDriverWait(driver, 15)


    email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email_field.send_keys(EMAIL)


    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys(PASSWORD)

    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    sign_in_button.click()

    
    try:
        profile_icon = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@class, 'global-nav__me-photo')]")
        ))
        print("[SUCCESS] Logged in to LinkedIn successfully.")
        driver.save_screenshot("linkedin_login_success.png")
        print("[INFO] Screenshot saved as linkedin_login_success.png.")
    except TimeoutException:
        print("[ERROR] Login may have failed. Check credentials or if captcha appeared.")


    try:
        captcha_element = driver.find_element(By.CLASS_NAME, "captcha-internal")
        print("[CAPTCHA DETECTED] Please solve it manually in the browser. Script paused.")
        input("Press Enter to continue after solving the captcha...")
    except NoSuchElementException:
        pass

except Exception as e:
    print(f"[EXCEPTION] An error occurred: {e}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    driver.quit()
