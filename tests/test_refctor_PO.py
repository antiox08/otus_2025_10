from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.comparison_page import ComparisonPage
from page_objects.wishlist_page import WishlistPage
from page_objects.alert_element import AlertSuccessElement
from test_data import TEST_USER


def test_add_to_wish_list(browser):
    browser.get(browser.base_url)
    product_name = MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_wish_list()
    AlertSuccessElement(browser).login.click()
    UserPage(browser).login(TEST_USER["email"], TEST_USER["password"])
    UserPage(browser).wait_logged_in()
    UserPage(browser).click_wish_list()
    WishlistPage(browser).wait_for_product_in_wish_list(product_name)


def test_add_to_cart(browser):
    browser.get(browser.base_url)
    product_name = MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_cart()
    AlertSuccessElement(browser).shoping_cart_click()
    CartPage(browser).wait_for_product_in_cart(product_name)
    CartPage(browser).click_checkout()
    CheckoutPage(browser).click_login_page()
    UserPage(browser).login(TEST_USER["email"], TEST_USER["password"])
    CheckoutPage(browser).wait_page_load()


def test_add_to_cart_from_comparison(browser):
    browser.get(browser.base_url)
    product_name = MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_comparison()
    AlertSuccessElement(browser).comparison.click()
    ComparisonPage(browser).wait_for_product_in_comparison(product_name)
    ComparisonPage(browser).click_confirm()
    AlertSuccessElement(browser).shoping_cart.click()
    CartPage(browser).wait_for_product_in_cart(product_name)
    CartPage(browser).click_checkout()
    CheckoutPage(browser).click_login_page()
    UserPage(browser).login(TEST_USER["email"], TEST_USER["password"])
    CheckoutPage(browser).wait_payment_form()
