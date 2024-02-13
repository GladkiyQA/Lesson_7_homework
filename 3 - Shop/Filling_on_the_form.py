class FillingForm:

    def __init__(self, browser):
        self.driver = browser

    def filling_on_the_form(self):
        self.driver.find_element('xpath', '//input[@id="first-name"]').send_keys("Dan")
        self.driver.find_element('xpath', '//input[@id="last-name"]').send_keys("Smooth")
        self.driver.find_element('xpath', '//input[@id="postal-code"]').send_keys('1234')
        self.driver.find_element('xpath', '//input[@id="continue"]').click()

    def get_final_price(self):
       total_price = self.driver.find_element('xpath', '//div[@class="summary_info_label summary_total_label"]')
       return total_price.text