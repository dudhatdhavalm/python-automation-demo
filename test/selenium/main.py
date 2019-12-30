from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome("./driver/chromedriver.exe")

browser.get("https://www.facebook.com/")
browser.implicitly_wait(30)

email = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("loginbutton")

email.send_keys("XXXXX")
password.send_keys("XXXXX")
submit.click()

page_title = browser.title
assert "Facebook" in page_title
browser.close()
