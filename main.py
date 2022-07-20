from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# fill in details
USERNAME = "username"
PASSWORD = "password"
CHROME_DRIVER_PATH = "find file and copy file path"
GENSHIN_LOGIN_URL = "daily login url"

ser = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=ser)
driver.get(GENSHIN_LOGIN_URL)

avatar_btn = driver.find_element(By.CSS_SELECTOR, '.components-home-assets-__sign-header_---avatar---2Zo35h')
avatar_btn.click()

sleep(1)
username_and_password = driver.find_elements(By.CSS_SELECTOR, '.mhy-account-flow-form-input div input')
username_field = username_and_password[0]
username_field.send_keys(USERNAME)
password_field = username_and_password[1]
password_field.send_keys(PASSWORD)
submit_btn = driver.find_element(By.CSS_SELECTOR, '.login-btn')
submit_btn.click()

sleep(15)
reward_btn = driver.find_element(By.CSS_SELECTOR, ".components-home-assets-__sign-content_---active---36unD3")
reward_btn.click()

driver.quit()
