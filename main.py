from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
# import keyring

# using HTTP so the captive portal can intercept with the connection
test_link = "http://neverssl.com/"
prefix = "auto-logger:"

username = input("Username: ")
pasword = getpass()

browser = webdriver.Safari()

browser.get(test_link)
print(prefix, "Success")

time.sleep(5)

web_username = browser.find_element(By.NAME, "username")
web_password = browser.find_element(By.NAME, "password")

print(prefix, "Success input data")

web_username.send_keys(username)
web_password.send_keys(pasword)

web_password.send_keys(Keys.ENTER)



browser.quit()

