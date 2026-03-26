import os
import random
import re
import allure
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


@allure.suite("PIM Module")
@allure.feature("Employee Management")
@allure.story("Add New Employee")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Tests the full flow of adding a new employee with a profile picture.")
def test_add_employee_successfully(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PIMPage(page)

    with allure.step("Navigate to Login and Enter Credentials"):
        login_page.navigate()
        login_page.login("Admin", "admin123")

    with allure.step("Navigate to PIM Section"):
        dashboard_page.navigate_to_pim()
        dashboard_page.click_add_employee()

    with allure.step("Generate Employee Data and Fill Form"):
        emp_id = str(random.randint(10000, 99999))
        # Ensure the 'assets' folder exists in your project root!
        photo_path = os.path.abspath("assets/my_pic.jpg")

        # Attach the photo path to the report for visibility
        allure.attach(f"Using Employee ID: {emp_id}", name="Employee Metadata",
                      attachment_type=allure.attachment_type.TEXT)

        pim_page.fill_employee_details("Anju", "Tester", emp_id, photo_path)

    with allure.step("Verify Success Toast and Redirect"):
        # We use wait_for_load_state to ensure the save request finished
        page.wait_for_load_state("networkidle")

        assert pim_page.verify_success(), "Success toast message was not displayed!"
        expect(page).to_have_url(re.compile(r".*viewPersonalDetails.*"))