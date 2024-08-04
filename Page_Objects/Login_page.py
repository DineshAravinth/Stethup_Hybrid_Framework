from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:

    login_click = (By.XPATH, "//span[contains(., 'Login' )]")
    textfield_email = (By.ID, "email")
    textfield_password = (By.ID, "password")
    button_login = (By.XPATH, "//button[@type='submit'][1]")
    icon_logout = (By.XPATH, "//h6[contains(@class,'nav-link register_font logut-de')]")
    dashboard_button = (By.XPATH,"//a[contains(.,'My Dashboard')]")
    register_button = (By.XPATH, "//a[contains(., 'Register for Free')]")
    welcome=(By.XPATH,"//h1[contains(.,'Welcome!')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    def login_action(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.login_click)).click()
        except TimeoutException as e:
            raise AssertionError("Login button not found or not clickable") from e

    def set_username(self, username):
        try:
            email_field = self.wait.until(EC.visibility_of_element_located(self.textfield_email))
            email_field.clear()
            email_field.send_keys(username)
        except TimeoutException as e:
            raise AssertionError("Email field not found or not visible") from e

    def set_password(self, password):
        try:
            password_field = self.wait.until(EC.visibility_of_element_located(self.textfield_password))
            password_field.clear()
            password_field.send_keys(password)
        except TimeoutException as e:
            raise AssertionError("Password field not found or not visible") from e

    def logging(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.button_login)).click()
        except TimeoutException as e:
            raise AssertionError("Login button not found or not clickable") from e

    def logout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.icon_logout)).click()
        except TimeoutException as e:
            raise AssertionError("Logout icon not found or not clickable") from e

    def is_dashboard_displayed(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.dashboard_button)).is_displayed()
        except TimeoutException:
            return False

    def is_welcome_displayed(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.welcome)).is_displayed()
        except TimeoutException:
            return False
