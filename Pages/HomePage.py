from Pages.BasePage import BaseFather
from Pages.Rokomari import Rokomari
from Pages.Rokomari_Social_SSO import Rokomari_SSO


class HomePage(BaseFather):

    def __init__(self, driver):
        super().__init__(driver)

    def navigation_to_signin_signup(self):
        self.click("Hom_modal_xpath")
        self.click("sign_in_sign_up_xpath")
        return Rokomari_SSO(self.driver)

    def Search(self, bookname):
        self.click("Hom_modal_xpath")
        self.type_on("Hom_search_input_xpath", bookname)
        self.click("Hom_search_submit_xpath")
        return self

    def Get_Search_Result(self, bookname):
        Rok_0 = Rokomari(self.driver)
        result = Rok_0.rok_book_info_extractor_from_search_result(bookname)
        return result
