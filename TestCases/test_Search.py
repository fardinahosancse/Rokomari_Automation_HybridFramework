from TestCases.Distribue import Distribute
from Pages.HomePage import HomePage
import logging
from Utility.LogUtil import Logger
import pytest

log = Logger(__name__, logging.INFO)


class Test_Search(Distribute):

    # Criteria :
    # 1. Search by Book Name
    # 2. Search by Publisher
    # 3. Search by Author

    def test_login_using_Stock_book_name(self, get_browser):
        driver = get_browser
        bookName = "ইকারাস"
        Home = HomePage(driver)
        Home.Search(bookName)
        result = Home.Get_Search_Result(bookName)
        assert result == True, f"No Book Found : Unexpected Error : {result} is suppose to be 'True' "

    def test_login_using_UnStock_book_name(self, get_browser):
        driver = get_browser
        bookName = "Cypress The Cat"
        Home = HomePage(driver)
        Home.Search(bookName)
        result = Home.Get_Search_Result(bookName)
        assert result == False, f"Book Found : Unexpected Error : {result} is suppose to be 'False' "

    def test_login_using_valid_publisher_name(self, get_browser):
        driver = get_browser
        pubName = "বাতিঘর প্রকাশনী"
        bookName = "নেমেসিস"
        Home = HomePage(driver)
        Home.Search(pubName)
        result = Home.Get_Search_Result(bookName)
        assert result == True, f"No Book Found : Unexpected Error : {result} is suppose to be 'True' "

    def test_login_using_invalid_publisher_name(self, get_browser):
        driver = get_browser
        pubName = "ইসলামিক ফাউন্ডেশন"
        bookName = "নেমেসিস"
        Home = HomePage(driver)
        Home.Search(pubName)
        result = Home.Get_Search_Result(bookName)
        assert result == False, f"Book Found : Unexpected Error : {result} is suppose to be 'False' "

    def test_login_using_valid_author_name(self, get_browser):
        driver = get_browser
        authorName = "মুহম্মদ জাফর ইকবাল"
        bookName = "অপারেশন নীলাঞ্জনা"
        Home = HomePage(driver)
        Home.Search(authorName)
        result = Home.Get_Search_Result(bookName)
        assert result == True, f"No Book Found : Unexpected Error : {result} is suppose to be 'True' "

    def test_login_using_invalid_author_name(self, get_browser):
        driver = get_browser
        authorName = "গোলাম মুরশিদ"
        bookName = "অপারেশন নীলাঞ্জনা"
        Home = HomePage(driver)
        Home.Search(authorName)
        result = Home.Get_Search_Result(bookName)
        assert result == False, f"Book Found : Unexpected Error : {result} is suppose to be 'False' "
