from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utility import configReader as conf
import logging
from Utility.LogUtil import Logger

log = Logger(__name__, logging.INFO)
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseFather:
    def __init__(self, driver):
        self.driver = driver

    # Responsible For Clicking Element
    def click(self, syntax):
        if syntax.endswith("_xpath"):
            try:
                # Create a WebDriverWait instance
                wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

                # Use WebDriverWait to wait for the element to be clickable
                element = wait.until(EC.element_to_be_clickable((By.XPATH, conf.readConfig("locatorsData", syntax))))

                # Click the element
                element.click()
                log.logger.info("Clicked on the element with XPath: " + syntax)

            except Exception as e:
                log.logger.error(f"Error clicking on element with XPath {syntax}: {str(e)}")
        else:
            log.logger.warning(f"Invalid syntax: {syntax}")

    # Responsible for Typing On a input field
    def type_on(self, syntex, syntex_value):
        if str(syntex).endswith("_xpath"):
            try:
                # Create a WebDriverWait instance
                wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

                # Use WebDriverWait to wait for the element to be typeable
                element = wait.until(EC.element_to_be_clickable((By.XPATH, conf.readConfig("locatorsData", syntex))))

                # Click the element
                element.send_keys(syntex_value)
                log.logger.info("Typed on the element with XPath: " + syntex)

            except Exception as e:
                log.logger.error(f"Error Typing on element with XPath {syntex}: {str(e)}")
        else:
            log.logger.warning(f"Invalid syntax: {syntex}")




    # Text Extractor from Element
    def get_text_from_element(self, syntax):
        if syntax.endswith("_xpath"):
            try:
                # Create a WebDriverWait instance
                wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

                # Use WebDriverWait to wait for the element to be clickable
                element = wait.until(EC.element_to_be_clickable((By.XPATH, conf.readConfig("locatorsData", syntax)))).text

                # Click the element
                return element

            except Exception as e:
                log.logger.error(f"Error Findih on element with XPath {syntax}: {str(e)}")
        else:
            log.logger.warning(f"Invalid syntax: {syntax}")


