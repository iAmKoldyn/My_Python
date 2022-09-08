import time
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
url = 'https://shop.silpo.ua/category/135'
driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get(url=url)
main_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-list-item')))
article = main_.find_element_by_class_name('product-title')
print(article)

time.sleep(5)
driver.close()
driver.quit()
