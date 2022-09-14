from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys



def main():

    driver = webdriver.Chrome()
    driver.get('https://store.steampowered.com/?l=russian')
    sleep(1)
    search = driver.find_element_by_xpath('//*[@id="store_nav_search_term"]')
    search.send_keys("action")
    sleep(3)
    search.send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="TagFilter_Container"]/div[1]/span[1]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="TagFilter_Container"]/div[4]/span[1]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="additional_search_options"]/div[8]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="narrow_byVR"]/div[1]/span[1]').click()
    # print(driver.current_url)
    sleep(5)
    scheight = .1
    while scheight < 9.9:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight += .01
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height'))
        driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()