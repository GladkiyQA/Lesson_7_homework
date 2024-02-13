class GetItems:

    def __init__(self, browser):
        self.driver = browser

    def get_items(self):
        self.driver.find_element('xpath', '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element('xpath', '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element('xpath', '//button[@id="add-to-cart-sauce-labs-onesie"]').click()

    def go_to_cart(self):
        self.driver.find_element('xpath', '//div[@id="shopping_cart_container"]').click()

    def checkout(self):
        self.driver.find_element('xpath', '//button[@id="checkout"]').click()
