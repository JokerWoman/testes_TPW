import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser =webdriver.Chrome()
        self.browser.maximize_window()  # Abre a página em grande para nao ter problemas com o hamburguer
        self.browser.get('http://localhost:8080/')
        self.browser.implicitly_wait(15)


    def tearDown(self):
        self.browser.quit()

    def test_View_Bolsas(self):
        login = self.browser.find_element_by_xpath('//a[text()="Entrar"]')
        login.click()

        loginP = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/small/a')
        loginP.click()

        professorUsername = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[1]/input')
        professorUsername.send_keys('Admin')

        password = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[2]/input')
        password.send_keys('Esmad_2021')

        login_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[4]/button')
        login_btn.click()

        bolsas = self.browser.find_element_by_xpath('//*[@id="nav-collapse"]/ul[1]/li[3]/a')
        bolsas.click()


        viewBolsa = self.browser.find_element_by_xpath('//*[@id="cardEvent2"]/div/a/button')
        viewBolsa.click()

    def test_editBolsa(self):
        login = self.browser.find_element_by_xpath('//a[text()="Entrar"]')
        login.click()

        loginP = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/small/a')
        loginP.click()

        professorUsername = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div/form/div[1]/input')
        professorUsername.send_keys('Admin')

        password = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[2]/input')
        password.send_keys('Esmad_2021')

        login_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[4]/button')
        login_btn.click()

        bolsas = self.browser.find_element_by_xpath('//*[@id="nav-collapse"]/ul[1]/li[3]/a')
        bolsas.click()

        editBolsa = self.browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/article/div/a/button')
        editBolsa.click()

        description = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/textarea')
        description.clear()
        description.send_keys("oferta(edit)")

        submitBtn = self.browser.find_element_by_xpath('//*[@id="editBolsaModal___BV_modal_body_"]/form/div[5]/button[1]')
        submitBtn.click()

    def test_createBolsa(self):
        login = self.browser.find_element_by_xpath('//a[text()="Entrar"]')
        login.click()

        loginP = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/small/a')
        loginP.click()

        professorUsername = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div/form/div[1]/input')
        professorUsername.send_keys('Admin')

        password = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[2]/input')
        password.send_keys('Esmad_2021')

        login_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[4]/button')
        login_btn.click()

        bolsas = self.browser.find_element_by_xpath('//*[@id="nav-collapse"]/ul[1]/li[3]/a')
        bolsas.click()

        createBtn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/button')
        createBtn.click()

        description = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/textarea')
        description.send_keys("Oferta")

        image = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[2]/div[1]/input')
        image.send_keys("https://media-exp1.licdn.com/dms/image/C4D0BAQENxzWcIgPK4g/company-logo_200_200/0/1593595898739?e=2159024400&v=beta&t=h3Hcd6RBtkOo560E_u2O9BZfbQYbLbfvVtRSGQEcFqI")

        offerLink = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[2]/div[2]/input')
        offerLink.send_keys("https://media-exp1.licdn.com/dms/image/C4D0BAQENxzWcIgPK4g/company-logo_200_200/0/1593595898739?e=2159024400&v=beta&t=h3Hcd6RBtkOo560E_u2O9BZfbQYbLbfvVtRSGQEcFqI")

        job = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[3]/div[1]/select')
        jobSelect = Select(job)
        jobSelect.select_by_value("1")

        company = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[3]/div[2]/select')
        companySelect = Select(company)
        companySelect.select_by_value("1")

        date = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[4]/div/input')
        date.send_keys("2020-06-23")

        submitBtn=self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[5]/button')
        submitBtn.click()

    def test_deleteBolsa(self):
        login = self.browser.find_element_by_xpath('//a[text()="Entrar"]')
        login.click()

        loginP = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/small/a')
        loginP.click()

        professorUsername = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div/form/div[1]/input')
        professorUsername.send_keys('Admin')

        password = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[2]/input')
        password.send_keys('Esmad_2021')

        login_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/div[4]/button')
        login_btn.click()

        bolsas = self.browser.find_element_by_xpath('//*[@id="nav-collapse"]/ul[1]/li[3]/a')
        bolsas.click()

        editBolsa = self.browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/article[1]/div/button')
        editBolsa.click()

        deleteBolsa=self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div[5]/button[2]')
        deleteBolsa.click()
        


