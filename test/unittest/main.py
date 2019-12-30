import unittest
from selenium import webdriver


class FacebookLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
        self.driver.implicitly_wait(30)

    def test_execute(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        email = driver.find_element_by_id("email")
        password = driver.find_element_by_id("pass")
        email.send_keys("XXXXX")
        password.send_keys("XXXXX")
        login_button = driver.find_element_by_id("loginbutton")
        login_button.click()
        assert "Facebook" in driver.title

    def tearDown(self):
        self.driver.close()


if(__name__ == "__main__"):
    unittest.main()
