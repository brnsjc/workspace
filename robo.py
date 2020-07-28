from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import csv
# driver = webdriver.Firefox(executable_path = "C:/Users/bruno moreira/Downloads/geckodriver-v0.24.0-win64/geckodriver.exe")

browser = webdriver.Firefox()

r = open("tel.csv", "r")

reader = csv.reader(r)

fones = []

for row in reader:
    fones.append(row)

# session_id = driver.session_id

url = "https://web.whatsapp.com/"
clique = True

browser.get(url)

time.sleep(20)

# clique = browser.find_element_by_class_name("_3j7s9").click()


def digitar_contato():
    try:
        browser.find_element_by_class_name("_3j7s9").click()
    except NoSuchElementException:
        return False
def procurar_nome():

    try:
        browser.find_element_by_class_name("_3j7s9")
    except NoSuchElementException:
        return False
def enviar_mensagem():
    browser.find_element_by_class_name("_3j7s9").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div").click()

numeros_nao_encontrado = []
fones = ['1234567890','1234567890','1234567890','1234567890','Monique']
# clique = digitar_contato()

for item in fones:
    pesquisa = browser.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").send_keys(item)
    time.sleep(5)
    username = procurar_nome()
    if username:
        clique = digitar_contato()
        time.sleep(5)
        #txtTarefa = browser.find_element_by_class_name("_1Plpp")
        #txtArea = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div").click()

        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").clear()
    else:
        print("numero nao encontrado")
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").clear()
        numeros_nao_encontrado.append(item)
        fones.remove(item)
print(numeros_nao_encontrado)
# print(browser.find_elements_by_class_name("X7YrQ"))

# txtTarefa = browser.find_element_by_class_name("_1Plpp")

# txtArea = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

# browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div").click()

# browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/#input").send_keys(os.getcwd() + "/julinho.jpeg")

# time.sleep(10)

# enviar = browser.find_element_by_class_name("TI3qN _2Mg6D").send_keys("")

# enviar.click()

# enviar.send_keys("teste")

# browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()
