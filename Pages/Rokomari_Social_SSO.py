# Often Rokomari uses single sign-on (SSO) system .
# Service Provider : Auth0 or Okta
import time
from Utility.configReader import readConfig as RC
from Pages.BasePage import BaseFather
from Utility.OTPRetriver import otp_catcher_gmail


class Rokomari_SSO(BaseFather):

    def __init__(self, driver):
        super().__init__(driver)

    def sign_up_valid(self, phone):
        self.type_on("email_phone_input_xpath", phone)
        self.click("next_xpath")
        time.sleep(4)
        username = RC("Auth","username")
        password = RC("Auth","password")
        otp = otp_catcher_gmail(username, password)
        self.type_on("otp_input_xpath", otp)
        time.sleep(5)
        self.click("submit_login_xpath")

    def sign_up_invalid(self, phone):
        self.type_on("email_phone_input_xpath", phone)
        self.click("next_xpath")
        time.sleep(4)
        self.type_on("otp_input_xpath", "0101")
        time.sleep(5)
        self.click("submit_login_xpath")
