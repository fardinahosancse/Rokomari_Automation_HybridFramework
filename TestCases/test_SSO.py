from TestCases.Distribue import Distribute
from Pages.HomePage import HomePage
from Pages.Rokomari import Rokomari
import logging
from Utility.LogUtil import Logger
from Utility.configReader import readConfig as RC

log = Logger(__name__, logging.INFO)


class Test_SSO(Distribute):

    def test_SignUp_with_valid_otp(self, get_browser):

        # Initialization
        driver = get_browser
        Home = HomePage(driver)
        RokomariXUTIL=Rokomari(driver)
        signup_mail =RC("Auth","signin_up")

        # Navigation
        Home.\
            navigation_to_signin_signup().\
            sign_up_valid(signup_mail)

        # Assertion
        expected_page_title="Buy Book Online - Best Online Book Shop in Bangladesh | Rokomari.com"
        assert RokomariXUTIL.rok_page_title() == expected_page_title,"OTP Unsuccessfull"

    def test_SignUp_with_invalid_otp(self, get_browser):

        # Initialization
        driver = get_browser
        Home = HomePage(driver)
        RokomariXUTIL=Rokomari(driver)
        signup_mail = RC("Auth", "signin_up")

        # Navigation
        Home.\
            navigation_to_signin_signup().\
            sign_up_invalid(signup_mail)

        # Assertion
        expected_page_title="Login To Rokomari | Rokomari.com"
        assert RokomariXUTIL.rok_page_title() == expected_page_title,f"Successfuly Registered/Login : Unexpected Error : {RokomariXUTIL.rok_page_title()} : is suppose to be: '{expected_page_title}' "

    def test_SignUp_with_invalid_mail(self, get_browser):

        # Initialization
        driver = get_browser
        Home = HomePage(driver)
        RokomariXUTIL=Rokomari(driver)

        # Navigation
        Home.\
            navigation_to_signin_signup().\
            sign_up_invalid("cswecswcc")

        # Assertion
        expected_page_title="Login To Rokomari | Rokomari.com"
        assert RokomariXUTIL.rok_page_title() == expected_page_title,f"Successfuly Registered/Login : Unexpected Error : {RokomariXUTIL.rok_page_title()} : is suppose to be: '{expected_page_title}' "

    def test_SignUp_with_blank_mail(self, get_browser):

        # Initialization
        driver = get_browser
        Home = HomePage(driver)
        RokomariXUTIL=Rokomari(driver)

        # Navigation
        Home.\
            navigation_to_signin_signup().\
            sign_up_invalid("")

        # Assertion
        expected_page_title="Login To Rokomari | Rokomari.com"
        assert RokomariXUTIL.rok_page_title() == expected_page_title,f"Successfuly Registered/Login : Unexpected Error : {RokomariXUTIL.rok_page_title()} : is suppose to be: '{expected_page_title}' "
