from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    IPHONE_CATEGORY = By.XPATH('//*[@id="wrapper"]//nav/text()')

    def open_main_page(self):
        self.open_page()

    def verify_opened_gettop(self):
        self.get_title_and_verify('gettop.us – Just another WordPress site')

    def click_on_category_iphone(self):
        self.open_page(end_url='/product-category/iphone/')

    def verify_opened_iphone_category(self):
        self.verify_text('Iphone', *self.IPHONE_CATEGORY)