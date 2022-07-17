import time

from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    PRODUCT_STOCK = (By.CSS_SELECTOR, '.product-small .product-title')
    PRODUCT_ASSET_DETAILS = (By.CSS_SELECTOR, 'h1')
    global ele

    def capture_product_title(self):
        ele = self.capture_random_text(*self.PRODUCT_STOCK)

    def click_on_product(self):
        ele.click()

    # def verify_product_page_opened2(self):
    #     self.verify_text(self.text3, *self.PRODUCT_ASSET_DETAILS)
