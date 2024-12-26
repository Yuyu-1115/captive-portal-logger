from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from getpass import getpass

from output import output
# import keyring

# using HTTP so the captive portal can intercept with the connection
test_link = "http://neverssl.com/"
prefix = "auto-logger:"

username = input("Username: ")
pasword = getpass()

browser = webdriver.Safari()

browser.get(test_link)
if browser.current_url == test_link:
    output("Redirection failed. Please check your network connection or check if you're already logged-in")
else:
    print(prefix, "Successfully redirect to", browser.current_url)
    try:
        web_username = browser.find_element(By.NAME, "username")
        web_password = browser.find_element(By.NAME, "password")
    except NoSuchElementException:
        print(prefix, "ERROR:", "Element not found")
    else:
        print(prefix, r"Successfully located the element 'username' and 'password' ")

        # pass the data in
        web_username.send_keys(username)
        web_password.send_keys(pasword)
        # enter to trigger login
        web_password.send_keys(Keys.ENTER)


    


browser.quit()

