import pytest
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Page_Objects.Registration_page import Registration_page
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_001_Register:

    url = Readconfig.get_url()

    def verify_element(self, ele_name):
        # Check if ele_name is a tuple (locator)
        #Purpose: A WebElement is an object that represents an element on a web page. It is returned by Selenium's methods like find_element_by_*.
        #Usage: If ele_name is a WebElement, it means the element has already been located, and the method can directly check its properties.
        if isinstance(ele_name, tuple):
            try:
                # Explicit wait to ensure element is present
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(ele_name)
                )
                return element.is_displayed()
            except TimeoutException:
                raise AssertionError("Element Is Not Present")

        # If ele_name is a WebElement
        elif hasattr(ele_name, 'is_displayed'): #This checks if ele_name is a WebElement by verifying if it has the is_displayed method.  hasattr Function: This built-in Python function checks if an object has a particular attribute.
            return ele_name.is_displayed()
        else:
            raise TypeError("ele_name must be a tuple (locator) or a WebElement")

    def verify_title(self, e_title, a_title, method_name):
        if e_title != a_title:
            self.save_screenshot(method_name)
            assert e_title == a_title, f"Title verification failed for {method_name}"


    def test_homepage1(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title,"test_login_initial")
        print("Login page is displayed")

    def test_register(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(2)
        self.reg=Registration_page(self.driver)
        sleep(2)
        self.reg.register_button()
        sleep(2)
        self.verify_title("StethUp: Your Partner in Achieving Your Healthcare Goals", self.driver.title,"test_register")
        print("Register page title is verified")

        #Enter the data into the text field
        if self.verify_element(Registration_page.first_name_field):
            self.reg.firstname("Dinesh")
        sleep(2)
        if self.verify_element(Registration_page.last_name_field):
            self.reg.lastname("Aravinth")
        sleep(2)
        if self.verify_element(Registration_page.Phonenum_field):
            self.reg.phonenumber(9994397426)
        sleep(2)
        if self.verify_element(Registration_page.email_field):
            self.reg.email("daravinth32@gmail.com")
        sleep(2)
        if self.verify_element(Registration_page.affiliation_dropdown):
            self.reg.affiliation("Registered Doctor")
        sleep(2)
        if self.verify_element(Registration_page.password_field):
            self.reg.password("asd@123")
        sleep(2)
        if self.verify_element(Registration_page.confirm_password_field):
            self.reg.confirm_password("asd@123")
        sleep(2)
        # if self.verify_element(Registration_page.agree_checkbox):
        #         self.reg.agree_tick()
        sleep(2)
        if self.verify_element(Registration_page.registration_button):
            self.reg.register()
        sleep(30)
        self.driver.quit()






