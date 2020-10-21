#Marcelo Aguiar Coelho de Moura Filho

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Page(object):
    def __init__(self, selenium_driver, base_url='http://training-wheels-protocol.herokuapp.com/nice_iframe'):
        self.base_url = base_url        
        self.driver = selenium_driver
        self.timeout = 30

 
    def find_element(self, *loc):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.presenceOfElement(*loc))
        return self.driver.find_element(*loc)
    
    def switch_frame(self, *loc):
        return self.driver.switch_to.frame(self.find_element(*loc))
        #driver.switch_to.frame
    def get_page(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def maximize_window(self):
        return self.driver.maximize_window()