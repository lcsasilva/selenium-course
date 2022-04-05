import os
from selenium import webdriver

os.environ['PATH'] += r"C:\workspace\py-se-booking"
driver = webdriver.Chrome()
driver.get('https://www.myinstants.com/instant/to-be-continued-jojo/')
my_element = driver.find_element_by_id('instant-page-button')
my_element.click()