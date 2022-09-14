from selenium import webdriver
from time import sleep


login = 'Naurlox'
password = '75yu4375'

def main():
    driver = webdriver.Chrome()
    driver.get('https://yummyanime.org/')

    register = driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]').click()
    sleep(1)
    login_input = driver.find_element_by_id("login_name")
    login_input.clear()
    login_input.send_keys(login)
    sleep(1)
    login_passward = driver.find_element_by_id("login_password")
    login_input.clear()
    login_passward.send_keys(password)
    sleep(1)
    driver.find_element_by_id("login_not_save").click()
    sleep(1)
    enter = driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/div[3]/button').click()
    sleep(1)
    genres_list = driver.find_element_by_xpath('/html/body/div[1]/div/div/aside/div[1]/ul/li[1]').click()
    sleep(1)
    our_genres = driver.find_element_by_xpath('/html/body/div[1]/div/div/aside/div[1]/ul/li[1]/ul/li[18]').click()
    sleep(1)
    anime_title6= driver.find_element_by_xpath('//*[@id="pagination"]/div/a[5]').click()
    sleep(1)
    our_anime = driver.execute_script("window.scrollTo(0, Y)")
    sleep(1)
    comment_сolumn= driver.find_element_by_xpath('//*[@id="dle-content"]/a[8]/div[1]/img').click()
    sleep(1)
    comment = driver.find_element_by_xpath('//*[@id="add-comments-form"]/div[1]/div/div/div/div[1]/div[2]')
    comment.send_keys('ВАНПИС в СЕРДЕЧКЕ')
    sleep(15)
    comment.submit()
if __name__ == '__main__':
    main()


# жанры детское 6ястраница 8е аниме  //*[@id="add-comments-form"]/div[1]/div/div/div/div[1]/div[2]