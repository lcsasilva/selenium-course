import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
driver.implicitly_wait(5)

email = driver.find_element_by_id('email')
passwd = driver.find_element_by_id('passwd')
btn = driver.find_element_by_css_selector('button[id="SubmitLogin"]')

email.send_keys('testeq1w2e3r4@teste.com')
passwd.send_keys('q1w2e3r4')
btn.click()

try:
    my_adress = driver.find_element_by_class_name('col-lg-4')
    my_adress.click()
    try:
        mobile_phone = driver.find_element_by_class_name('address_phone_mobile')
        print(f'Celular {mobile_phone.text}')
    except:
        print('Número não encontrado')
except:
    print('Lista de desejos não encontrada.')