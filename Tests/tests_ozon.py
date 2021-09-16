import time

from ozon import SearchHelper


def test_ozon_search(browser):
    """ вставка текста в поиск запроса"""
    ozon_main_page = SearchHelper(browser)
    ozon_main_page.go_to_site()
    ozon_main_page.enter_word("смартфон pixel 4a")
    ozon_main_page.click_on_the_search_button()
    return None


def test_check_result_of_search(browser):
    """проверка результата поиска"""
    ozon_main_page = SearchHelper(browser)
    ozon_main_page.go_to_site()
    ozon_main_page.enter_word("блендер")
    ozon_main_page.click_on_the_search_button()


def test_ozon_catalog(browser):
    """проверка каталога"""
    ozon_catalog_page = SearchHelper(browser)
    ozon_catalog_page.go_to_site()
    ozon_catalog_page.click_catalog()
    ozon_catalog_page.click_elektronika()
    return None


def test_ozon_search_and_screenshot(browser):
    """ скриншот поиска"""
    ozon_main_page = SearchHelper(browser)
    ozon_main_page.go_to_site()
    ozon_main_page.enter_word("брелок")
    ozon_main_page.click_on_the_search_button()
    ozon_main_page.highlight_and_make_screenshot()
    return None


def test_ozon_button_of_shopcart(browser):
    ozon_main_page = SearchHelper(browser)
    ozon_main_page.go_to_site()
    ozon_main_page.click_shopcart()
    return None


def test_ozon_button_of_favorites(browser):
    ozon_main_page = SearchHelper(browser)
    ozon_main_page.go_to_site()
    ozon_main_page.click_follow()
    assert None
