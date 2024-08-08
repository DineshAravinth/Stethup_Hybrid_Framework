from time import sleep
import pytest
from selenium import webdriver
from Page_Objects.Login_page import LoginPage
from datetime import datetime
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_001_Login:

    url = Readconfig.get_url()
    username = Readconfig.get_email()
    password = Readconfig.get_password()
    logger = LogGen.loggen()

    def save_screenshot(self, method_name):
        d = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        screenshot_path = f"/Users/apple/Automation/STETHUP_PROJECT/Screenshots/{method_name}_{d}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"*** {method_name} title failed ***")
        return f"Screenshot saved to {screenshot_path}"

    def verify_title(self, e_title, a_title, method_name):
        if e_title != a_title:
            self.save_screenshot(method_name)
            assert e_title == a_title, f"Title verification failed for {method_name}"

    # @pytest.mark.dependency()
    def test_loginpage(self,setup):
        self.logger.info("*** Test_001_Login ***")
        self.logger.info("*** Verify Loginpage Title ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title,"test_login_initial")
        self.logger.info("*** Loginpage title is passed ***")
        # print("Login page is displayed")


    # @pytest.mark.dependency(depends=["Test_001_Login::test_loginpage"])
    def test_homepage(self,setup):
        self.logger.info("*** Test_001_Login ***")
        self.logger.info("*** Verify Home page Title ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp= LoginPage(self.driver)
        self.lp.login_action()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.logging()
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title,"test_login_Homepage")
        self.logger.info("*** Homepage title is passed ***")
        # print("Home page is displayed")
        sleep(3)
        self.lp.logout()
        self.logger.info("**** LOGOUT SUCCESFULLY ****")
        # print("logout Successfully")
        sleep(3)