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
from Utilities.customLogger import LogGen

class Test_001_Post_Job:
    url = Readconfig.get_url()
    logger = LogGen.loggen()
    path = "/Users/apple/Automation/STETHUP_PROJECT/Test_Data/DDT_Data.xlsx"
    sheet_name = "postjob"
    job_image="/Users/apple/Downloads/1720001920747.png"

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

    def test_Post_Job(self, setup):
        self.logger.info("*** Posting_A_Job ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Login actions
        self.lp = LoginPage(self.driver)
        self.lp.login_action()
        self.lp.set_username(Readconfig.get_email())  # Updated method name
        self.lp.set_password(Readconfig.get_password())
        self.lp.logging()

        # Verify title after login
        self.verify_title("stethUP: Connecting You to the Future of Healthcare", self.driver.title, "test_Post_Job")
        self.logger.info("*** Jobs Page Title is Passed ***")
        self.logger.info("*** Jobs Page is displayed ***")
        sleep(3)

        # Verify Post Job page display
        self.logger.info("*** Verify Post Jobs page display ***")
        self.jb = Job_Post(self.driver)
        self.jb.dashboard_button()
        self.jb.skip()
        self.jb.employer_profile()
        sleep(3)
        self.jb.regular_job_button()
        sleep(3)
        self.verify_title("Transform Your Medical Journey with Unlimited Courses", self.driver.title, "test_Post_Job")
        self.logger.info("*** Verify Post Jobs page is Passed ***")
        self.logger.info("*** Post Jobs page is displayed ***")

        row_count = Excel_Utilities.getRowCount(self.path, self.sheet_name)
        headings = Excel_Utilities.readHeadings(self.path, self.sheet_name)

        for row in range(2, row_count + 1):
            title_in_excel = Excel_Utilities.readData(self.path, self.sheet_name, row, 1)  # Column A
            data_to_enter = Excel_Utilities.readData(self.path, self.sheet_name, row, 3)  # Column C

            # Verify the title
            if title_in_excel == "Hire For Whom":
                self.jb.hire_for_whom(data_to_enter)
                sleep(3)
            elif title_in_excel == "Organization Name":
                self.jb.org_name(data_to_enter)
                sleep(3)
            elif title_in_excel == "Job Title":
                self.jb.job_title(data_to_enter)
                sleep(3)
            elif title_in_excel == "Category":
                self.jb.category(data_to_enter)
                sleep(3)
            elif title_in_excel == "Job Post Category":
                self.jb.job_post(data_to_enter)
                sleep(3)
            elif title_in_excel == "Employment Type":
                self.jb.employment(data_to_enter)
                sleep(3)
            elif title_in_excel == "Sector":
                sectors_list = [sec.strip() for sec in data_to_enter.split(',')]
                assert isinstance(sectors_list, list), f"Sectors list is not properly formatted at row {row}."
                self.jb.sector(sectors_list)
                sleep(3)
            elif title_in_excel == "Job Description":
                self.jb.job_description(data_to_enter)
                sleep(3)
            elif title_in_excel == "Min Experience":
                self.jb.minimum_experience(data_to_enter)
                sleep(3)
            elif title_in_excel == "Max Experience":
                self.jb.maximum_experience(data_to_enter)
                sleep(3)
            elif title_in_excel == "Total Positions":
                self.jb.total_position(data_to_enter)
                sleep(3)
            elif title_in_excel == "Qualification":
                self.jb.qualification(data_to_enter)
                sleep(3)
            elif title_in_excel == "Designation":
                self.jb.designation(data_to_enter)
                sleep(3)
            elif title_in_excel == "Job Posting Date":
                self.jb.job_posting(data_to_enter)
                sleep(3)
            elif title_in_excel == "Job Closing Date":
                self.jb.job_closing(data_to_enter)
                sleep(3)
            elif title_in_excel == "License Required":
                self.jb.license(data_to_enter)
                sleep(3)
            elif title_in_excel == "Shift Availability":
                self.jb.shift_ava(data_to_enter)
                sleep(3)
            elif title_in_excel == "Joining Time":
                self.jb.joining_time(data_to_enter)
                sleep(3)
            else:
                self.logger.error(f"Unknown title '{title_in_excel}' in Excel. Skipping entry.")
                continue

        self.jb.file_upload(self.job_image)
        sleep(5)
        self.jb.next_button()
        self.logger.info(f"*** Page 1 Job_Post is successfull")

        sleep(5)













'''
# Mapping of Excel titles to corresponding methods and verification methods
mapping = {
    "Hire For Whom": ("hire_for_whom", "get_hire_for_whom"),
    "Organization Name": ("org_name", "get_org_name"),
    "Job Title": ("job_title", "get_job_title"),
    "Category": ("category", "get_category"),
    "Job Post Category": ("job_post", "get_job_post"),
    "Employment Type": ("employment", "get_employment"),
    "Sector": ("sector", "get_sector"),
    "Job Description": ("job_description", "get_job_description"),
    "Min Experience": ("minimum_experience", "get_minimum_experience"),
    "Max Experience": ("maximum_experience", "get_maximum_experience"),
    "Total Positions": ("total_position", "get_total_position"),
    "Qualification": ("qualification", "get_qualification"),
    "Designation": ("designation", "get_designation"),
    "Job Posting Date": ("job_posting", "get_job_posting"),
    "Job Closing Date": ("job_closing", "get_job_closing"),
    "License Required": ("license", "get_license"),
    "Shift Availability": ("shift_ava", "get_shift_ava"),
    "Joining Time": ("joining_time", "get_joining_time"),
}

for row in range(2, row_count + 1):
    title_in_excel = Excel_Utilities.readData(self.path, self.sheet_name, row, 1)  # Column A
    data_to_enter = Excel_Utilities.readData(self.path, self.sheet_name, row, 3)  # Column B

    if title_in_excel in mapping:
        method_name, get_method_name = mapping[title_in_excel]
        method = getattr(self.jb, method_name)

        # If "Sector", special case as it expects a list
        if title_in_excel == "Sector":
            data_to_enter = [sec.strip() for sec in data_to_enter.split(',')]

        # Call the method to enter data
        method(data_to_enter)
        sleep(3)

        # Verify the entered data
        get_method = getattr(self.jb, get_method_name)
        entered_data = get_method()
        assert entered_data == data_to_enter, f"Data mismatch for {title_in_excel}: expected {data_to_enter}, got {entered_data}"
    else:
        self.logger.error(f"Unknown title '{title_in_excel}' in Excel. Skipping entry.")
        continue
'''
