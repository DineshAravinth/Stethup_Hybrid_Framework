import pytest
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Page_Objects.Registration_page import Registration_page
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import Excel_Utilities
from datetime import datetime

class Test_001_Register_DTT:
    url = Readconfig.get_url()
    path = "/Users/apple/Automation/STETHUP_PROJECT/Test_Data/DDT_Data.xlsx"

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

    def test_homepage1(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title, "test_login_initial")
        print("Login page is displayed")

    def test_register(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(2)
        self.reg = Registration_page(self.driver)
        sleep(2)
        self.reg.register_button()
        sleep(2)
        self.verify_title("StethUp: Your Partner in Achieving Your Healthcare Goals", self.driver.title, "test_register")
        print("Register page title is verified")

        expected_headings = ["First Name", "Last Name", "Phone", "Email", "Affiliation", "Password", "Confirm Password"]
        headings = Excel_Utilities.readHeadings(self.path, "register")

        # Validate headings
        for expected_heading in expected_headings:
            assert expected_heading in headings, f"Heading '{expected_heading}' is missing or incorrect in the Excel sheet"

        field_mapping = {
            "First Name": (Registration_page.first_name_field, self.reg.firstname),
            "Last Name": (Registration_page.last_name_field, self.reg.lastname),
            "Phone": (Registration_page.Phonenum_field, self.reg.phonenumber),
            "Email": (Registration_page.email_field, self.reg.email),
            "Affiliation": (Registration_page.affiliation_dropdown, self.reg.affiliation),
            "Password": (Registration_page.password_field, self.reg.password),
            "Confirm Password": (Registration_page.confirm_password_field, self.reg.confirm_password)
        }

        for field_name, (locator, method) in field_mapping.items():
            if field_name in headings:
                col = headings[field_name]
                data = Excel_Utilities.readData(self.path, "register", 2, col)
                if self.verify_element(locator):
                    method(data)
                sleep(2)

        sleep(2)
        if self.verify_element(Registration_page.registration_button):
            self.reg.register()
        sleep(5)
