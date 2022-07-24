from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
import time

@then ('Choose product and capture product title')
def capture_product_title(context):
    context.app.product_page.capture_product_title2()

@when('Click on product')
def click_on_product(context):
    context.app.product_page.click_on_product2()

@then('Verify that correct product page is opened')
def verify_product_page_opened(context):
    context.app.product_page.verify_product_page_opened2()