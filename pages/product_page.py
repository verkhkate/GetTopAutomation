import time

from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    PRODUCT_STOCK_TITLES = (By.CSS_SELECTOR, '.product-small .product-title')
    PRODUCT_STOCK_PICS = (By.CSS_SELECTOR, '.box-image a[href*="https://gettop.us/product/"]')
    PRODUCT_ASSET_DETAILS = (By.CSS_SELECTOR, 'h1')
    random_element = None
    random_title = None

    def capture_product_title2(self):
        self.random_title, self.random_element = self.capture_random_element(self.PRODUCT_STOCK_TITLES, self.PRODUCT_STOCK_PICS)

    def click_on_product2(self):
        self.random_element.click()
        print(self.random_element, self.random_title)

    def verify_product_page_opened2(self):
        self.verify_text(self.random_title, *self.PRODUCT_ASSET_DETAILS)
