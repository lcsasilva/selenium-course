import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r"C:\workspace\py-se-booking"
driver = webdriver.Chrome()
driver.get('https://www.myinstants.com/instant/to-be-continued-jojo/')
driver.implicitly_wait(3)
my_element = driver.find_element_by_id('instant-page-button')
my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'instant-page-title') ,# Element Filtration
        'Complete!'# The expected text
    )
)