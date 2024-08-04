from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Registration_page:
    register_button_click = (By.XPATH,"//span[.='Join for Free']")
    first_name_field = (By.ID,"first_name")
    last_name_field = (By.ID,"last_name")
    Phonenum_field = (By.NAME,"phone_no")
    email_field = (By.ID,"uniqueEmail")
    password_field = (By.ID,"password1")
    confirm_password_field = (By.ID,"password2")
    affiliation_dropdown = (By.XPATH,"//select[@id='i_am_a']")
    agree_checkbox=(By.XPATH,"//label[@class='checkbox-custom-label']")
    registration_button=(By.XPATH,"(//button[@type='submit'])[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    def register_button(self):
        # Wait for the register button to be present
        sleep(5)
        self.wait.until(EC.presence_of_element_located(self.register_button_click))
        # Scroll to the register button
        # element = self.driver.find_element(*self.register_button_click)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # Wait for the register button to be clickable and then click it
        self.wait.until(EC.element_to_be_clickable(self.register_button_click)).click()

    def firstname(self,firstname):
        first_name= self.wait.until(EC.visibility_of_element_located(self.first_name_field))
        first_name.clear()
        first_name.send_keys(firstname)

    def lastname(self,lastname):
        last_name= self.wait.until(EC.visibility_of_element_located(self.last_name_field))
        last_name.clear()
        last_name.send_keys(lastname)

    def phonenumber(self,phonenumber):
        phone_number= self.wait.until(EC.visibility_of_element_located(self.Phonenum_field))
        sleep(2)
        #phone_number.clear()
        phone_number.send_keys(phonenumber)

    def email(self,email):
        emailid= self.wait.until(EC.visibility_of_element_located(self.email_field))
        # emailid.clear()
        sleep(3)
        emailid.send_keys(email)

    def password(self,password1):
        pass1= self.wait.until(EC.visibility_of_element_located(self.password_field))
        pass1.clear()
        pass1.send_keys(password1)

    def confirm_password(self,password2):
        pass2= self.wait.until(EC.visibility_of_element_located(self.confirm_password_field))
        pass2.clear()
        pass2.send_keys(password2)

    def affiliation(self,field):
        aff=self.wait.until((EC.visibility_of_element_located(self.affiliation_dropdown)))
        # aff.click()
        s_obj=Select(aff)
        s_obj.select_by_visible_text(field)

    def agree_tick(self):
        sleep(3)
        agree = self.wait.until(EC.visibility_of_element_located(self.agree_checkbox))
        sleep(3)
        agree.click()
    def register(self):
        regi=self.wait.until(EC.visibility_of_element_located(self.registration_button))
        regi.click()


