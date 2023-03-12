import requests
import openpyxl
import json
import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def issue_request(url, path, method, data=None, headers=None):
    full_url = f'{url}/{path}'
    response = requests.request(
        method=method,
        url=full_url,
        json=data,
        headers=headers
    )
    return response

def read_xls_file(file, sheet):
    wb = openpyxl.open(file)
    return [list(r) for r in wb[sheet].iter_rows(min_row=2, values_only=True)]
    
def get_json_values_by_key(file, key):
    with open(file) as f:
        json_objects = json.load(f)
        try:
            return json_objects[key]
        except KeyError as e:
            logging.error(f"{key} was not found.")

class DriverFunctions():

    wait_timeout = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait_driver = WebDriverWait(driver, self.wait_timeout)

    def open_page(self, url):
        self.driver.get(url)

    def find_element_by_name(self, selector):
        return self.wait_driver.until(EC.visibility_of_element_located((By.NAME, selector)))

    def find_element_by_id(self, selector):
        return self.wait_driver.until(EC.visibility_of_element_located((By.ID, selector)))

    def find_elements_by_id(self, selector):
        return self.driver.find_elements(By.ID, selector)

    def find_element_by_xpath(self, selector):
        return self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, selector)))

    def find_element_by_link_text(self, selector):
        return self.driver.find_element(By.LINK_TEXT, selector)

    def action_hover_element(self, element_to_hover):
        return ActionChains(self.driver).move_to_element(element_to_hover).perform()

    def action_move_to_element_and_click(self, element_to_click):
        return ActionChains(self.driver).move_to_element(element_to_click).click().perform()

    def close(self):
        return self.driver.quit()