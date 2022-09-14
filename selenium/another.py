# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get('http://matrix.itasoftware.com/')
# elem = driver.find_element_by_xpath(
#     './/input[@id="ita_form_date_DateTextBox_0"]'
#     '/following-sibling::input[@type="hidden"]')

# value = driver.execute_script('return arguments[0].value;', elem)
# print("Before update, hidden input value = {}".format(value))

# driver.execute_script('''
#     var elem = arguments[0];
#     var value = arguments[1];
#     elem.value = value;
# ''', elem, '2013-11-26')

# value = driver.execute_script('return arguments[0].value;', elem)
# print("After update, hidden input value = {}".format(value))


from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup   
from lxml import html
import requests
 
# genre = input()

driver = webdriver.Chrome()
driver.get('https://store.steampowered.com/?l=russian')

search = driver.find_element_by_xpath('//*[@id="store_nav_search_term"]')

search.send_keys("стратегии")
sleep(3)
search.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="TagFilter_Container"]/div[1]/span[1]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="TagFilter_Container"]/div[10]/span[1]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="TagFilter_Container"]/div[4]/span[1]').click()
soup = BeautifulSoup("lxml")

games_link = soup.find('div', {'class': 'nameRus'}).find('a').get('href')
# games_desc = soup.find('div', {'class': 'nameRus'}).find('a').text

# games_links = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]
# games_desc = item_lxml.xpath('.//div[@class = "nameRus"]/a/text()')[0]
# games_list = driver.find_elements_by_class_name
sleep(150)


# //*[@id="TagFilter_Container"]/div[4]/span[1]

driver.close()
driver.quit()