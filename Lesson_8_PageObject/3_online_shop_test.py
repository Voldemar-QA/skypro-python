from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.online_shop_home import HomePage
from pages.online_shop_goods import GoodsPage
from pages.online_shop_cart import CartPage
from pages.online_shop_checkout import CheckoutPage
from pages.online_shop_overview import OverviewPage


user_name = "standard_user"
parol = "secret_sauce"
var_first_name = "John"
var_last_name = "Doe"
var_zip = "135813"


def test_online_shop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=options)

    online_shop_home = HomePage(browser)
    online_shop_home.username(user_name)
    online_shop_home.password(parol)
    online_shop_home.login()

    online_shop_goods = GoodsPage(browser)
    online_shop_goods.backpack()
    online_shop_goods.tshirt()
    online_shop_goods.onesie()
    online_shop_goods.cart_btn()

    online_shop_cart = CartPage(browser)
    online_shop_cart.checkout_btn()

    online_shop_checkout = CheckoutPage(browser)
    online_shop_checkout.first_name(var_first_name)
    online_shop_checkout.last_name(var_last_name)
    online_shop_checkout.zip(var_zip)
    online_shop_checkout.summary()

    online_shop_overview = OverviewPage(browser)
    sum = online_shop_overview.total()
    assert sum == "$58.29"
    print(sum)

    sleep(2)
    browser.quit
