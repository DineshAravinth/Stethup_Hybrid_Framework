from time import sleep
import pytest
from datetime import datetime
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import Excel_Utilities
from Page_Objects.Login_page import LoginPage


class Test_002_DDT_Login:
    url = Readconfig.get_url()
    logger = LogGen.loggen()
    path = "/Users/apple/Automation/STETHUP_PROJECT/Test_Data/DDT_Data.xlsx"

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

    def test_loginpage_DTT(self, setup):
        self.logger.info("*** Test_002_Login_page_DTT ***")
        self.logger.info("*** Verify Login_page Title ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title,
                          "test_login_initial")
        self.logger.info("*** Login_page title is Passed ***")

    def test_homepage_DTT(self, setup):
        self.logger.info("*** Test_002_Homepage(Jobs_Page)_DDT ***")
        self.logger.info("*** Verify Home_page(Jobs_Page) Title ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = Excel_Utilities.getRowCount(self.path, "Sheet1")
        print("no. of rows in excel", self.rows)

        for r in range(2,self.rows + 1):
            self.user = Excel_Utilities.readData(self.path, "Sheet1", r, 1)
            self.password = Excel_Utilities.readData(self.path, "Sheet1", r, 2)
            self.exp = Excel_Utilities.readData(self.path, "Sheet1", r, 3)

            self.driver.get(self.url)
            self.lp.login_action()
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.logging()
            sleep(3)

            is_dashboard_displayed = self.lp.is_dashboard_displayed()
            is_welcome_displayed = self.lp.is_welcome_displayed()

            if self.exp == "Pass":
                if is_dashboard_displayed:
                    self.logger.info("**** Login test passed(Jobs_page is displayed) ****")
                    assert True
                    self.lp.logout()
                else:
                    self.logger.error("**** Login test failed(Jobs_page is not displayed) ****")
                    self.save_screenshot(f"test_homepage_DTT_row_{r}")
                    assert False, "Dashboard should be displayed for valid credentials"
            elif self.exp == "Fail":
                if not is_dashboard_displayed:
                    self.logger.info("**** Invalid_Credentials login_test is passed(Login_page is displayed) ****")
                    assert True
                else:
                    self.logger.error("**** Invalid login test failed(Jobs_page is displayed) ****")
                    self.save_screenshot(f"test_homepage_DTT_row_{r}")
                    assert False, "Dashboard should not be displayed for invalid credentials"

                if is_welcome_displayed:
                    self.logger.info("**** Invalid credentials and login page(Welcome_text) is displayed ****")
                else:
                    self.logger.error("**** Jobs page is displaed ((login_page) welcome text is not displayed) ****")
                    self.save_screenshot(f"test_homepage_DTT_row_{r}_register_button")
                    assert False, "Invalid credentials but home_page(Jobs page) is displayed"

            sleep(5)

        self.driver.quit()
