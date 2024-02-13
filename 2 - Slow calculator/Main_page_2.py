from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculator:

    def __init__(self):
        options = Options()
        options.add_argument("--window-size=1000,1000")  # Если хочется визуала
        # options.add_argument("--headless")
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 60, 1)

    def open_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    def delay_form(self, num):
        delay_field = self.driver.find_element('xpath', '//input[@id="delay"]')
        delay_field.clear()
        delay_field.send_keys(num)


    def click_button(self, button):
        self.driver.find_element('xpath', f'//span[text()="{button}"]').click()

    def get_result(self, button):
        APPEARANCE_RESULT = ('xpath', f'//div[text()="{button}"]')
        self.wait.until(EC.visibility_of_element_located(APPEARANCE_RESULT))
        finally_result = self.driver.find_element(*APPEARANCE_RESULT).text

        return finally_result


