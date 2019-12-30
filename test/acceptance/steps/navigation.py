from behave import *
from selenium import webdriver
import os

use_step_matcher("re")


@given("Open Facebook home page")
def open_home_page(context):
    context.browser = webdriver.Chrome("./driver/chromedriver.exe")
    context.browser.get("https://www.facebook.com")
    context.browser.implicitly_wait(30)


@when("Enter login details")
def read_title_page(context):
    email = context.browser.find_element_by_id("email")
    password = context.browser.find_element_by_id("pass")
    email.clear()
    email.send_keys("XXXXX")
    password.clear()
    password.send_keys("XXXXX")
    login_button = context.browser.find_element_by_id("loginbutton")
    login_button.click()


@then("Verify page title")
def verify_page(context):
    assert "Facebook" in context.title
