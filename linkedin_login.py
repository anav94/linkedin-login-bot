from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os


EMAIL = "your_email"
PASSWORD = "your_password"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


driver = webdriver.Chrome(options=options)

try:
    
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)  


    driver.find_element(By.ID, "username").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)


    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)  


    success = False
    try:
   
        driver.find_element(By.XPATH, "//img[contains(@class, 'global-nav__me-photo')]")
        success = True
        print("[SUCCESS] Logged in to LinkedIn successfully.")
        
        driver.save_screenshot("linkedin_login_success.png")
        print("[INFO] Screenshot saved as linkedin_login_success.png.")
    except NoSuchElementException:
        print("[ERROR] Login may have failed. Check credentials or if captcha appeared.")
    
    try:
        captcha = driver.find_element(By.CLASS_NAME, "captcha-internal")
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

