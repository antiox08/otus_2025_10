from page_objects.admin.admin_login_page import AdminLoginPage
from page_objects.admin.admin_menu import AdminMenuPage
from page_objects.admin.admin_product_page import AdminProductPage
from page_objects.admin.admin_add_product_page import AdminAddProductPage
from page_objects.admin.admin_alert import AlertSuccessElement
from page_objects.admin.admin_customer_page import AdminCustomerPage
from page_objects.admin.admin_add_customer_page import AdminAddCustomerPage
from test_data import ADMIN_USER


def test_add_and_del_product(browser):
    # Открываем страницу админки
    browser.get(f"{browser.base_url}/administration/")

    # Логинимся
    login_page = AdminLoginPage(browser)
    login_page.login(ADMIN_USER["username"], ADMIN_USER["password"])
    login_page.wait_logged_in()

    # Переход в меню
    menu_page = AdminMenuPage(browser)
    menu_page.click_to_catalog_product()

    # Переход на страницу продуктов
    product_page = AdminProductPage(browser)
    product_page.wait_page_basket()
    product_page.page_add_product()

    # Создание продукта
    add_product_page = AdminAddProductPage(browser)
    add_product_page.add_product()
    add_product_page.add_model()
    add_product_page.add_seo()
    add_product_page.save_product()
    add_product_page.return_to_product_list()

    # Удаление продукта
    del_product = AdminProductPage(browser)
    del_product.click_checkbox()
    del_product.click_basket()

    # Успешные алерты
    alert = AlertSuccessElement(browser)
    alert.confirm_alert()
    alert._wait()

def test_add_customer(browser):
    browser.get(f"{browser.base_url}/administration")

    login_page = AdminLoginPage(browser)
    login_page.login(ADMIN_USER["username"], ADMIN_USER["password"])
    login_page.wait_logged_in()

    menu_page = AdminMenuPage(browser)
    menu_page.click_to_customers()

    customer_page = AdminCustomerPage(browser)
    customer_page.wait_page_basket()
    customer_page.page_add_customers()

    add_customer_page = AdminAddCustomerPage(browser)
    alert = AlertSuccessElement(browser)
    add_customer_page.add_customer()
    add_customer_page.save_customer()
    alert._wait()

    menu_page.click_to_customers()
    customer_page.wait_user_in_list("Test", "Test")