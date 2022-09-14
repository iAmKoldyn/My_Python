from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


login = 'Naurlox'
password = '75yu4375'

def main():

    driver = webdriver.Chrome()
    driver.get('https://yummyanime.org/')

    register = driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]').click()
    sleep(1)
    login_input = driver.find_element_by_id("login_name")
    login_input.send_keys(login)
    sleep(1)
    login_passward = driver.find_element_by_id("login_password")
    login_passward.send_keys(password)
    sleep(1)
    driver.find_element_by_id("login_not_save").click()
    sleep(1)
    enter = driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/div[3]/button').click()
    sleep(1)
    genres_list = driver.find_element_by_xpath('/html/body/div[1]/div/div/aside/div[1]/ul/li[1]').click()
    sleep(1)
    our_genres = driver.find_element_by_xpath('/html/body/div[1]/div/div/aside/div[1]/ul/li[1]/ul/li[18]/a').click()
    sleep(1)
    anime_title6= driver.find_element_by_xpath('//*[@id="pagination"]/div/a[5]').click()
    sleep(3)
    comment_сolumn= driver.find_element_by_xpath('//*[@id="dle-content"]/a[8]/div[1]/img').click()
    sleep(2)
    our_anime = driver.execute_script("window.scrollTo(0, 3000)")
    sleep(3)
    column= driver.find_element_by_xpath('//*[@id="add-comments-form"]/div[2]/div/button').click()
    sleep(1)

    elem = driver.find_element_by_xpath('//*[@id="_mce_caret"]') # name поля
    elem.clear()
    elem.send_keys("text you need to send") # текст комментария
    elem.send_keys(Keys.RETURN)

    driver.close()
    # tinymce = driver.find_element_by_id('tinymce')  //*[@id="_mce_caret"]
    # tinymce.send_keys('стратегии')

    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()

# жанры детское 6ястраница 8е аниме


# com = driver.xpath('//*[@id="tinymce"]')
# com.click()
# com.send_keys('qwe')