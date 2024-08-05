import pytest
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Page_Objects.Job_Post_page1_JD import Job_Post
from Page_Objects.Login_page import LoginPage
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import Excel_Utilities
from datetime import datetime

class Test_001_:
    url = Readconfig.get_url()
    path = "/Users/apple/Automation/STETHUP_PROJECT/Test_Data/DDT_Data.xlsx"
    logger = LogGen.loggen()

    def verify_element(self, ele_name):
        if isinstance(ele_name, tuple):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(ele_name)
                )
                return element.is_displayed()
            except TimeoutException:
                raise AssertionError("Element Is Not Present")
        elif hasattr(ele_name, 'is_displayed'):
            return ele_name.is_displayed()
        else:
            raise TypeError("ele_name must be a tuple (locator) or a WebElement")

    def verify_title(self, e_title, a_title, method_name):
        if e_title != a_title:
            self.save_screenshot(method_name)
            assert e_title == a_title, f"Title verification failed for {method_name}"

    def test_Post_Job(self,setup):
        self.logger.info("*** Posting_A_Job ***")
        self.logger.info("*** Verify Jobs Page Title ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp= LoginPage(self.driver)
        self.lp.login_action()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.logging()
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title,"test_Post_Job")
        self.logger.info("*** Jobs Page Title is Passed ***")
        self.logger.info("*** Jobs Page is displayed ***")
        sleep(3)

        #to verify a post job page
        self.logger.info("*** Verify Post Jobs page display ***")
        self.jb= Job_Post(self.driver)
        self.jb.dashboard_button()
        self.jb.skip()
        self.jb.employer_profile()
        self.verify_title("Transform Your Medical Journey with Unlimited Courses", self.driver.title,"test_Post_Job")
        self.logger.info("*** Verify Post Jobs page is Passed ***")
        self.logger.info("*** Post Jobs page is displayed ***")

        # to post a job
        self.jb.regular_job_button()






