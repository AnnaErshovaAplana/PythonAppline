import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time


class TestSearch(unittest.TestCase):
    def setUp(self):
        print('start browser for test...')
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()

    def test_search_for_selenide(self):
        # Открыть страницу http://google.com/ncr
        self.driver.get("http://google.com/ncr")
        WebDriverWait(self.driver,5).until(EC.title_is('Google'),'title is not Google')
        assert self.driver.title == 'Google', 'window title is not "Google"'

        # Выполнить поиск слова “selenide”
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('selenide',Keys.RETURN)
        # Проверить, что первый результат – ссылка на сайт selenide.org.
        selenide_link = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]//link')
        assert 'selenide.org' in selenide_link.get_attribute('href'),'The first link does not contain "selenide.org"'
        time.sleep(3)
        # Перейти в раздел поиска изображений
        pictures_tab = self.driver.find_element_by_xpath('//a[@data-sc="I"]')
        pictures_tab.click()
        # Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        first_picture = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@data-ri="0"]/a[2]')))
        assert 'selenide.org' in first_picture.get_attribute('href'),'The first picture does not refer to "selenide.org"'
        time.sleep(3)
        # Вернуться в раздел поиска Все
        all_tab = self.driver.find_element_by_xpath('//a[contains(text(),"Все")]')
        all_tab.click()
        time.sleep(3)
        # Проверить, что первый результат такой же, как и на шаге 3.
        assert 'selenide.org' in self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]//link').get_attribute('href'),'The first link does not contain "selenide.org"'

    def tearDown(self):
        print('quit browser for test...')
        self.driver.quit()


if __name__=='__main__':
    unittest.main()