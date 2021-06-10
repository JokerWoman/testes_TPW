import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import  element_to_be_clickable
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window() #Abre a página em grande para nao ter problemas com o hamburguer
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.browser.implicitly_wait(15)
        self.browser.get('http://localhost:8080/')

    def tearDown(self):
        self.browser.quit()


    def test_Login(self):

      numero = '191800433'
      register = self.browser.find_element_by_xpath('//a[text()="Registro"]')
      register.click()

      nroEstudante_box = self.browser.find_element_by_css_selector('input#nroestudante')
      nroEstudante_box.send_keys(numero)

      email_box = self.browser.find_element_by_css_selector('input#email')
      email_box.send_keys('andrea@gmail.com')

      nome_box = self.browser.find_element_by_css_selector('input#nome')
      nome_box.send_keys('Nuno Silva')

      nome_box = self.browser.find_element_by_css_selector('input#morada')
      nome_box.send_keys('Rua das Namoradas')

      password_box = self.browser.find_element_by_css_selector('input#password')
      password_box.send_keys('1234')

      confirmpassword_box = self.browser.find_element_by_css_selector('input#confirmar')
      confirmpassword_box.send_keys('1234')

      cc_box = self.browser.find_element_by_css_selector('input#cc')
      cc_box.send_keys('123456789')

      data = self.browser.find_element_by_css_selector('input#data_Nasc')
      data.send_keys('08/07/1998')

      numero = self.browser.find_element_by_css_selector('input#numero')
      numero.send_keys('935993406')

      genero = self.browser.find_element_by_css_selector('input#generoF')
      genero.click()

      registar = self.browser.find_element_by_css_selector('button#registar')
      registar.click()