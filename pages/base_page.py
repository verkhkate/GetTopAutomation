from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import time



class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://gettop.us/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def capture_random_text(self, *locator):
        elements_list = self.driver.find_elements(*locator)
        random_element = random.choice(elements_list)
        # Converting Webelement to a simple text
        # random_element_text = randon_element.text
        # print(random_element.text)
        return random_element

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def get_title_and_verify(self, expected_text):
        title = self.driver.title
        # print(title)
        actual_text = title
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        print(actual_text)
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
           f'Expected text{expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'
