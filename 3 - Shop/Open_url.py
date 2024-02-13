

class ThingShop:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get('https://www.saucedemo.com/')

    def open_site(self):
        self.driver.find_element('xpath', '//input[@name="user-name"]').send_keys('standard_user')
        self.driver.find_element('xpath', '//input[@name="password"]').send_keys('secret_sauce')
        self.driver.find_element('xpath', '//input[@name="login-button"]').click()
