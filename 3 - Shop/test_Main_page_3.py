import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from Filling_on_the_form import FillingForm
from Open_url import ThingShop
from Get_items import GetItems

def test_shop():
    options = Options()
    options.add_argument("--window-size=2560,1600")  # Если хочется визуала
    # options.add_argument("--headless")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    thing_shop = ThingShop(driver)
    thing_shop.open_site()

    get_items = GetItems(driver)
    get_items.get_items()
    get_items.go_to_cart()
    get_items.checkout()

    filling_form = FillingForm(driver)
    filling_form.filling_on_the_form()
    a = filling_form.get_final_price()
    assert 'Total: $58.29' == a

