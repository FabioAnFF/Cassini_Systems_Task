from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.helpers import *

def before_all(context):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    context.driver_functions = DriverFunctions(webdriver.Chrome(chrome_options=chrome_options))

def after_all(context):
        context.driver_functions.close()
