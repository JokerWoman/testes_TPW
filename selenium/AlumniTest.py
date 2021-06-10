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


    # Login

        register = self.browser.find_element_by_xpath('//a[text()="Entrar"]')
        register.click()

        username_box = self.browser.find_element_by_css_selector('input#nroestudante')
        username_box.send_keys(19180048)

        password_box = self.browser.find_element_by_css_selector('input#password')
        password_box.send_keys('Esmad_2021')

        login_btn = self.browser.find_element_by_css_selector('button#login')
        login_btn.click()

    # Entrar ao Perfil


        sel = self.browser.find_element_by_css_selector("a[role='button']").click()

        sel2 = self.browser.find_element_by_xpath('//a[text()="Perfil"]')
        sel2.click()
    # Entrar ao Editar Perfil

        editarPerfil = self.browser.find_element_by_xpath('//a[text()="Editar Perfil"]')
        editarPerfil.click()
    # Escrever no textarea e guardar
        textarea = self.browser.find_element_by_xpath('//textarea')
        textarea.click()

        textarea2 = self.browser.find_element_by_tag_name('textarea')
        textarea2.send_keys('Ola! sou uma experaaaaaaasssssssaaaat!!!!')

        guardarDes = self.browser.find_element_by_xpath('//button[text()=" Guardar "]')
        guardarDes.click()

    # Adicionar um Portfolio

        editarPortefolio = self.browser.find_element_by_css_selector('a#editarPortefolio')
        editarPortefolio.click()

        addPortfolio = self.browser.find_element_by_css_selector('button#addPortfolio')
        addPortfolio.click()

        githubchoice = self.browser.find_element_by_xpath("//select/option[@value='1']")
        githubchoice.click()

        link_box = self.browser.find_element_by_css_selector('input#link')
        link_box.send_keys('https://github.com/JokerWoman')


        guardarLink2 = self.browser.find_element_by_xpath('//button[text()="Guardar"]')
        guardarLink2.click()

        guardarLink = self.browser.find_element_by_xpath('//button[text()=" Sair "]')
        guardarLink.click()

    # Adicionar um skill

        editarSkill = self.browser.find_element_by_css_selector('a#editarSkill')
        editarSkill.click()

        addSkill = self.browser.find_element_by_xpath('//button[text()=" Adicionar "]')
        addSkill.click()

        skillchoice = self.browser.find_element_by_xpath("//select/option[@value='1']")
        skillchoice.click()

        guardarSkill = self.browser.find_element_by_xpath('//button[text()="Guardar"]')
        guardarSkill.click()

    # Adiciona mais exp na skill

        editarSkill = self.browser.find_element_by_css_selector('button#mais')
        editarSkill.click()

        editarSkill2 = self.browser.find_element_by_css_selector('button#mais')
        editarSkill2.click()

        editarSkill3 = self.browser.find_element_by_css_selector('button#mais')
        editarSkill3.click()

        guardarSkillDef = self.browser.find_element_by_xpath('//button[text()=" Sair "]')
        guardarSkillDef.click()
































