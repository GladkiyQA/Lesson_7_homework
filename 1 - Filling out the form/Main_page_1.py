from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
class Fillng_form:
    def __init__(self):
        options = Options()
        options.add_argument("--window-size=2560,1600")  # Если хочется визуала
        # options.add_argument("--headless")
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def open_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def filling_out_the_form(self):
        form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # Оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

        for field, value in form_data.items():
            self.driver.find_element('xpath', f'//input[@name="{field}"]').send_keys(value)
        self.driver.find_element('xpath', '//button[@type="submit"]').click()

    def getting_values_for_zip(self):
        zip_code_field = self.driver.find_element('xpath', '//div[@id="zip-code"]')
        return zip_code_field.get_attribute('class')

    def getting_values_for_other_fields(self):
        other_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position",
                        "company"]
        for field in other_fields:
            input_field_full = self.driver.find_element('xpath', f'//div[@id="{field}"]')
            return input_field_full.get_attribute('class')

        def get_value_for_field(self, field):
            input_field_full = self.driver.find_element('xpath', f'//div[@id="{field}"]')
            return input_field_full.get_attribute('class')

        def get_values_for_fields(self, fields):
            values_dict = {}
            for field in fields:
                input_field_full = self.driver.find_element('xpath', f'//div[@id="{field}"]')
                values_dict[field] = input_field_full.get_attribute('class')
            return values_dict