from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from time import sleep
import datetime

class Job_Post:
    my_dashboard_button = (By.XPATH, "//a[contains(.,'My Dashboard')]")
    skip_click = (By.XPATH, "(//button[@type='button'])[1]")
    employer_profile_click = (By.XPATH, "(//a[contains(.,'Access Now')])[6]")
    add_regular_job_button = (By.XPATH, "//button[contains(.,'Add Regular Job')]")
    direct_employer_radio_button = (By.XPATH, "//span[contains(.,'Direct employer')]")
    recruitment_company_radio_button = (By.XPATH, "//span[contains(.,'Recruitment ')]")
    organisation_name_field = (By.ID, "Org_name")
    job_title_field = (By.ID, "job_title")
    category_dropdown = (By.ID, "vertical")
    custom_category = (By.ID, "customCateg")
    job_post_category_dropdown = (By.ID, "job_post")
    employment_dropdown = (By.ID, "job_type")
    sector_field = (By.ID, "search_input")
    sector_options = (By.XPATH, "//input[@id='search_input']/../following-sibling::div/ul/li")
    hospital_select = (By.XPATH, "//input[@id='search_input']/../following-sibling::div/ul/li[1]")
    job_description_field = (By.XPATH, "//div[@data-gramm='false']")
    min_exp_field = (By.ID, "min_experience")
    max_exp_field = (By.ID, "year_experience")
    total_positions_field = (By.ID, "total_positions")
    qualification_field = (By.ID, "Qualification")
    designation_field = (By.ID, "Designation")
    job_posting_date = (By.XPATH, "//input[@type='date' and @id='job_posting_date']")
    job_closing_date = (By.XPATH, "//input[@type='date' and @id='job_closing_date']")
    license_required_dropdown = (By.ID, "license_required")
    shift_availability_dropdown = (By.ID, "shift_availability")
    joining_time_dropdown = (By.ID, "joining_time")
    image_click = (By.ID, "img")
    next_button1_recruit = (By.XPATH, "//span[contains(.,'Next')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    def dashboard_button(self):
        dashboard = self.wait.until(EC.visibility_of_element_located(self.my_dashboard_button))
        assert dashboard is not None, "Dashboard button not found"
        dashboard.click()

    def skip(self):
        skipp = self.wait.until(EC.visibility_of_element_located(self.skip_click))
        assert skipp is not None, "Skip button not found"
        skipp.click()

    def employer_profile(self):
        emp = self.wait.until(EC.visibility_of_element_located(self.employer_profile_click))
        assert emp is not None, "Employer profile button not found"
        emp.click()

    def regular_job_button(self):
        regular = self.wait.until(EC.visibility_of_element_located(self.add_regular_job_button))
        assert regular is not None, "Add Regular Job button not found"
        regular.click()

    def hire_for_whom(self, value):
        if value == "Direct employer":
            direct_employer = self.wait.until(EC.visibility_of_element_located(self.direct_employer_radio_button))
            assert direct_employer is not None, "Direct employer radio button not found"
            direct_employer.click()
        elif value == "Recruitment company":
            recruitment_company = self.wait.until(EC.visibility_of_element_located(self.recruitment_company_radio_button))
            assert recruitment_company is not None, "Recruitment company radio button not found"
            recruitment_company.click()
        else:
            assert False, "Invalid value for hire_for_whom"

    def org_name(self, org):
        organisation = self.wait.until(EC.visibility_of_element_located(self.organisation_name_field))
        assert organisation is not None, "Organisation name field not found"
        organisation.clear()
        organisation.send_keys(org)

    def job_title(self, title):
        jobtitle = self.wait.until(EC.visibility_of_element_located(self.job_title_field))
        assert jobtitle is not None, "Job title field not found"
        jobtitle.clear()
        jobtitle.send_keys(title)

    def category(self, field):
        cate = self.wait.until(EC.visibility_of_element_located(self.category_dropdown))
        assert cate is not None, "Category dropdown not found"
        s_obj = Select(cate)
        if field in ["Medical", "Nursing", "Dentist", "Pharmacist", "Technicians", "Others"]:
            s_obj.select_by_visible_text(field)
            if field == "Others":
                cus_cate = self.wait.until(EC.visibility_of_element_located(self.custom_category))
                assert cus_cate is not None, "Custom category field not found"
                cus_cate.clear()
                cus_cate.send_keys(field)
        else:
            assert False, "Category not found"

    def job_post(self, job):
        jobpost = self.wait.until(EC.visibility_of_element_located(self.job_post_category_dropdown))
        assert jobpost is not None, "Job post category dropdown not found"
        s_obj = Select(jobpost)
        if job in ["Jobs", "Internship", "Fellowship", "Observership", "Residency"]:
            s_obj.select_by_visible_text(job)
        else:
            assert False, "Job post category not found"

    def employment(self, type):
        emptype = self.wait.until(EC.visibility_of_element_located(self.employment_dropdown))
        assert emptype is not None, "Employment dropdown not found"
        s_obj = Select(emptype)
        if type in ["Full Time", "Part Time", "Internship"]:
            s_obj.select_by_visible_text(type)
        else:
            assert False, "Employment type not found"

    def sector(self, sec_list):
        try:
            sector = self.wait.until(EC.visibility_of_element_located(self.sector_field))
            assert sector is not None, "Sector field not found"
            sector.click()
        except TimeoutException:
            print("TimeoutException: Sector field not found or not clickable")
            return

        action = ActionChains(self.driver)

        for sec in sec_list:
            sec = sec.strip()  # Remove any leading/trailing whitespace
            xpath = f"//ul/li[text()='{sec}']"
            option_found = False
            error_logged = False  # Flag to track if the error message has been logged

            for _ in range(10):  # Adjust range if necessary
                try:
                    sector_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                    assert sector_option is not None, f"{sec} option not found"
                    try:
                        sector_option.click()
                    except ElementClickInterceptedException:
                        # Click using JavaScript as a fallback
                        self.driver.execute_script("arguments[0].click();", sector_option)
                    option_found = True
                    break
                except TimeoutException:
                    if not error_logged:  # Log the error message only once per sector
                        print(f"TimeoutException: {sec} option not found, scrolling down")
                        error_logged = True
                    # Scroll down the dropdown
                    action.send_keys(Keys.ARROW_DOWN).perform()
                    sleep(0.2)  # Small delay for smooth scrolling
                except ElementClickInterceptedException:
                    if not error_logged:
                        print(f"ElementClickInterceptedException: Unable to click {sec} directly, scrolling down")
                        error_logged = True
                    action.send_keys(Keys.ARROW_DOWN).perform()
                    sleep(0.2)

            if not option_found:
                print(f"{sec} option not found after scrolling")

    def job_description(self, value):
        job_des = self.wait.until(EC.visibility_of_element_located(self.job_description_field))
        assert job_des is not None, "Job description field not found"
        job_des.clear()
        job_des.send_keys(value)

    def minimum_experience(self, mini):
        min_exp = self.wait.until(EC.visibility_of_element_located(self.min_exp_field))
        assert min_exp is not None, "Minimum experience field not found"
        min_exp.clear()
        min_exp.send_keys(mini)

    def maximum_experience(self, maxi):
        max_exp = self.wait.until(EC.visibility_of_element_located(self.max_exp_field))
        assert max_exp is not None, "Maximum experience field not found"
        max_exp.clear()
        max_exp.send_keys(maxi)

    def total_position(self, tot):
        total = self.wait.until(EC.visibility_of_element_located(self.total_positions_field))
        assert total is not None, "Total positions field not found"
        total.clear()
        total.send_keys(tot)

    def qualification(self, quali):
        qualifi = self.wait.until(EC.visibility_of_element_located(self.qualification_field))
        assert qualifi is not None, "Qualification field not found"
        qualifi.clear()
        qualifi.send_keys(quali)

    def designation(self, des):
        desi = self.wait.until(EC.visibility_of_element_located(self.designation_field))
        assert desi is not None, "Designation field not found"
        desi.clear()
        desi.send_keys(des)

    import datetime

    def job_posting(self, date):
        sleep(2)
        dat = self.wait.until(EC.visibility_of_element_located(self.job_posting_date))
        assert dat is not None, "Job posting date field not found"
        sleep(2)
        # Convert datetime to string before sending
        if isinstance(date, datetime.datetime):
            date_str = date.strftime("%d-%m-%Y")  # Adjust the format as required by the date picker
        else:
            date_str = str(date)

        # dat.clear()  # Uncomment if you need to clear the input field before entering the date
        dat.send_keys(date_str)
        sleep(2)

    def job_closing(self, date):
        sleep(2)
        dat = self.wait.until(EC.visibility_of_element_located(self.job_closing_date))
        assert dat is not None, "Job posting date field not found"
        sleep(2)
        # Convert datetime to string before sending
        if isinstance(date, datetime.datetime):
            date_str = date.strftime("%d-%m-%Y")  # Adjust the format as required by the date picker
        else:
            date_str = str(date)
        # dat.clear()  # Uncomment if you need to clear the input field before entering the date
        dat.send_keys(date_str)
        sleep(2)

    def license(self, type):
        lic = self.wait.until(EC.visibility_of_element_located(self.license_required_dropdown))
        assert lic is not None, "License required dropdown not found"
        s_obj = Select(lic)
        if type in ["Yes", "No"]:
            s_obj.select_by_visible_text(type)
        else:
            assert False, "License required option not found"

    def shift_ava(self, type):
        shift = self.wait.until(EC.visibility_of_element_located(self.shift_availability_dropdown))
        assert shift is not None, "Shift availability dropdown not found"
        s_obj = Select(shift)
        if type in ["Day", "Night", "Evening", "Rotational"]:
            s_obj.select_by_visible_text(type)
        else:
            assert False, "Shift availability option not found"

    def joining_time(self, type):
        join = self.wait.until(EC.visibility_of_element_located(self.joining_time_dropdown))
        assert join is not None, "Joining time dropdown not found"
        s_obj = Select(join)
        if type in ["Immediate", "One Month", "Two Months"]:
            s_obj.select_by_visible_text(type)
        else:
            assert False, "Joining time option not found"

    def file_upload(self, field):
        file = self.wait.until(EC.visibility_of_element_located(self.image_click))
        assert file is not None, "File upload element not found"
        file.send_keys(field)

    def next_button(self):
        sec = self.wait.until(EC.visibility_of_element_located(self.next_button1_recruit))
        assert sec is not None, "Next button not found"
        sec.click()
