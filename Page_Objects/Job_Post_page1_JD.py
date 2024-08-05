from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Job_Post:
    my_dashboard_button= (By.XPATH,"//a[contains(.,'My Dashboard')]")
    skip_click=(By.XPATH,"(//button[@type='button'])[1]")
    employer_profile_click=(By.XPATH,"(//a[contains(.,'Access Now')])[6]")
    add_regular_job_button=(By.XPATH,"//button[contains(.,'Add Regular Job')]")
    direct_employer_radio_button=(By.XPATH,"//span[contains(.,'Direct employer')]")
    recruitment_comany_radio_button=(By.XPATH,"//span[contains(.,'Recruitment ')])]")
    # organisation_name_text_name=(By.XPATH,"//label[contains(.,'Organization Name *')]")
    organisation_name_field=(By.ID,"Org_name")
    job_title_field=(By.Id,"job_title")
    category_dropdown=(By.Id,"vertical")
    custom_category =(By.ID,"customCateg")

    job_post_category_dropdown=(By.Id,"job_post")
    employment_dropdown=(By.Id,"job_type")
    sector_field=(By.Id,"search_input")
    hospital_select=(By.XPATH,"//input[@id='search_input']/../following-sibling::div/ul/li[1]")
    job_description_field =(By.XPATH,"//div[@data-gramm='false']")
    min_exp_field=(By.ID,"min_experience")
    max_exp_field=(By.ID,"year_experience")
    total_positions_field=(By.ID,"total_positions")
    qualification_field=(By.ID,"Qualification")
    designation_field=(By.ID,"Designation")
    job_posting_date=(By.XPATH,"//input[contains(@id,'job_posting_date')]")
    job_closing_date=(By.XPATH,"//input[contains(@id,'job_closing_date')]")
    license_required_dropdown=(By.Id,"license_required")
    shift_availability_dropdown=(By.Id,"shift_availability")
    joining_time_dropdown=(By.Id,"joining_time")
    image_click=(By.ID,"img")
    next_button1_recruit=(By.XPATH,"//span[contains(.,'Next')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    def dasboard_button(self):
        dashboard=self.wait.until(EC.visibility_of_element_located(self.my_dashboard_button))
        dashboard.click()
    def skip(self):
        skipp=self.wait.until(EC.visibility_of_element_located(self.skip_click))
        skipp.click()
    def employer_profile(self):
        emp = self.wait.until(EC.visibility_of_element_located(self.employer_profile_click))
        emp.click()
    def regular_job_button(self):
        regular = self.wait.until(EC.visibility_of_element_located(self.add_regular_job_button))
        regular.click()
    def hire_for_whom(self,value):
        if value ==  "Direct Employer":
            direct_employer = self.wait.until(EC.visibility_of_element_located(self.direct_employer_radio_button))
            direct_employer.click()
        elif vlaue == "Recruitment Company":
            recuritment_company = self.wait.until(EC.visibility_of_element_located(self.recruitment_comany_radio_button))
            recuritment_company.click()

    def org_name(self,org):
        organisation= self.wait.until(EC.visibility_of_element_located(self.organisation_name_field))
        organisation.clear()
        (organisation.send_keys(org))

    def job_title(self,title):
        jobtitle = self.wait.until(EC.visibility_of_element_located(self.job_title_field))
        jobtitle.clear()
        jobtitle.send_keys(title)

    def category(self,field):
        cate=self.wait.until((EC.visibility_of_element_located(self.category_dropdown)))
        s_obj=Select(cate)
        if field == "Medical":
            s_obj.select_by_visible_text("Medical")
        elif field == "Nursing":
            s_obj.select_by_visible_text("Nursing")
        elif field == "Dentist":
            s_obj.select_by_visible_text("Dentist")
        elif field == "Pharmacist":
            s_obj.select_by_visible_text("Pharmacist")
        elif field == "Technicians":
            s_obj.select_by_visible_text("Technicians")
        elif field == "Others":
            s_obj.select_by_visible_text("Others")
            cus_cate = self.wait.until(EC.visibility_of_element_located(self.custom_category))
            cus_cate.clear()
            (cus_cate.send_keys(field))
        else:
            assert False, "Category not found"
    def job_post(self,job):
        jobpost=self.wait.until((EC.visibility_of_element_located(self.job_post_category_dropdown)))
        s_obj=Select(jobpost)
        if job == "Jobs":
            s_obj.select_by_visible_text("Jobs")
        elif job == "Internship":
            s_obj.select_by_visible_text("Internship")
        elif job == "Fellowship":
            s_obj.select_by_visible_text("Fellowship")
        elif job == "Observership":
            s_obj.select_by_visible_text("Observership")
        elif job == "Residency":
            s_obj.select_by_visible_text("Residency")
        else:
            assert False,"Job Post category not found"

    employment_dropdown=(By.Id,"job_type")
    def employment(self,type):
        emptype=self.wait.until((EC.visibility_of_element_located(self.employment_dropdown)))
        s_obj=Select(emptype)
        if type == "Full Time":
            s_obj.select_by_visible_text("Full Time")
        elif type == "Part Time":
            s_obj.select_by_visible_text("Part Time")
        elif type == "Internship":
            s_obj.select_by_visible_text("Internship")
        else:
            assert False,"Employment type not found"

    def sector(self,sec):
        sec=self.wait.until((EC.visibility_of_element_located(self.employment_dropdown)))
        sec.click()

    def job_description(self,value):
        job_des=self.wait.until((EC.visibility_of_element_located(self.job_description_field)))
        job_des.clear()
        job_des.send_keys(value)
    def minimum_experience(self,mini):
        min_exp=self.wait.until((EC.visibility_of_element_located(self.min_exp_field)))
        min_exp.clear()
        min_exp.send_keys(mini)
    def maximum_experience(self,maxi):
        max_exp=self.wait.until((EC.visibility_of_element_located(self.max_exp_field)))
        max_exp.clear()
        max_exp.send_keys(maxi)
    def total_position(self,tot):
        total=self.wait.until((EC.visibility_of_element_located(self.total_positions_field)))
        total.clear()
        total.send_keys(tot)
    def qualification(self,quali):
        qualifi=self.wait.until((EC.visibility_of_element_located(self.qualification_field)))
        qualifi.clear()
        qualifi.send_keys(quali)
    def desgination(self,des):
        desi=self.wait.until((EC.visibility_of_element_located(self.designation_field)))
        desi.clear()
        desi.send_keys(des)

    def job_posting(self,date):
        dat = self.wait.until((EC.visibility_of_element_located(self.designation_field)))
        dat.send_keys(date)
    def job_closing(self,date):
        dat =self.wait.until((EC.visibility_of_element_located(self.designation_field)))
        dat.send_keys(date)

    def license(self,type):
        lic=self.wait.until((EC.visibility_of_element_located(self.license_required_dropdown)))
        s_obj=Select(lic)
        if type == "Yes":
            s_obj.select_by_visible_text("Yes")
        elif type == "No":
            s_obj.select_by_visible_text("No")
        else:
            assert False, "Not found"

    def shift_ava(self,type):
        shift = self.wait.until((EC.visibility_of_element_located(self.shift_availability_dropdown)))
        s_obj = Select(shift)
        if type == "Day":
            s_obj.select_by_visible_text("Day")
        elif type == "Night":
            s_obj.select_by_visible_text("Night")
        elif type == "Evening":
            s_obj.select_by_visible_text("Evening")
        elif type == "Rotational":
            s_obj.select_by_visible_text("Rotational")
        else:
            assert False, "not found"

    def joining_time(self,type):
        join = self.wait.until((EC.visibility_of_element_located(self.joining_time_dropdown)))
        s_obj = Select(join)
        if type == "Immediate":
            s_obj.select_by_visible_text("Immediate")
        elif type == "One month":
            s_obj.select_by_visible_text("One month")
        elif type == "Two months":
            s_obj.select_by_visible_text("Two months")
        else:
            assert False, "not found"
    def file_upload(self,field):
        file = self.wait.until((EC.visibility_of_element_located(self.file_upload())))
        dat.send_keys(field)
        























