from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('/usr/bin/chromedriver')
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import wait



driver.get("https://www.youtube.com/watch?v=w-P9rDTCFn4")
xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[5]/div[2]/div[2]/ytd-video-secondary-info-renderer/div/div/div/ytd-button-renderer/a/tp-yt-paper-button'

driver.find_element(by=By.XPATH, value=xpath).click()




# driver.get("https://web.telegram.org/k/#@bibinto_bot")
# time.sleep(1000)
# el = driver.find_element(By.XPATH, )
                                    
# el.click()
# time.sleep(1000)
# driver.quit()
# driver.find_element_by_xpath("//span[text()='Сообщение']")
# button = driver.find_element_by_xpath("//div[@class='s-btn']")
# button.click()

# while True:

#     while True:
#         # Если данные все еще загружаются, классы кнопки меняются на `s-btn__loader`
#         if driver.find_elements_by_class_name('s-btn__loader'):
#             time.sleep(5000)
#         else:
#             break

#     try:
#         load_more_btn = driver.find_element_by_xpath("//span[text()='Сообщение']")
#     except NoSuchElementException:
#         print('Загрузили страницу до конца')
#         break
    
#     load_more_btn.click()

#     time.sleep(5000)


# driver.findElements(By.xpath("//*[@id='column-center']/div/div/div[4]/div/div[5]/button']")).get(0).click
# driver.findElements(By.xpath(".//input[@class='button primary']")).get(0).click


# //*[@id="column-center"]/div/div/div[4]/div/div[5]/button/div
# /html/body/div[1]/div[1]/div[2]/div/div/div[4]/div/div[5]/button/div