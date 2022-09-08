from selenium import webdriver
from bs4 import BeautifulSoup

chromedriver = '/usr/local/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
# Переход на страницу входа
browser.get('http://playsports365.com/default.aspx')
# Поиск тегов по имени
email = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_UserName')
password = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_Password')
login = browser.find_element_by_name('ctl00$MainContent$ctlLogin$BtnSubmit')
# добавление учётных данных для входа
email.send_keys('********')
password.send_keys('*******')
# нажатие на кнопку отправки
login.click()
# После успешного входа в систему переходим на страницу «OpenBets»
browser.get('http://playsports365.com/wager/OpenBets.aspx')
# Получение HTML-содержимого
requiredHtml = browser.page_source
soup = BeautifulSoup(requiredHtml, 'html5lib')
table = soup.findChildren('table')
my_table = table[0]
# получение тегов и печать значений
rows = my_table.findChildren(['th', 'tr'])
for row in rows:
    cells = row.findChildren('td')
    for cell in cells:
        value = cell.text
        print (value)