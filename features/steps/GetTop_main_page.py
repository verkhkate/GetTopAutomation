from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
import time


@given('Open GetTop website home page')
def open_gettop(context):
    context.app.main_page.open_main_page()
    time.sleep(1)


@then('Verify that GetTop website home page is opened')
def verify_gettop_opened(context):
    context.app.main_page.verify_opened_gettop()


@when('Click on "IPHONE" category in the Header menu')
def click_on_iphone_category(context):
    context.app.main_page.click_on_category_iphone()


@then('Verify that "IPHONE" category page is opened')
def verify_iphone_category_opened(context):
    context.app.main_page.verify_opened_iphone_category()
