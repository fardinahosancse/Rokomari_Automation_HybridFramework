from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from Pages.BasePage import BaseFather
from Utility import configReader as conf


class Rokomari(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)

    def rok_book_info_extractor_from_search_result(self,bookname):
        wrap = self.driver.find_element(By.XPATH, conf.readConfig("locatorsData", "search_result_div_xpath"))
        book_titles = wrap.find_elements(By.TAG_NAME, "a")
        result=False

        for title in book_titles:
            if bookname in title.text:
                result=True

        return result

    def rok_page_title(self):
        return self.driver.title

