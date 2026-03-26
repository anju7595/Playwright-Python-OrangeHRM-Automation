import os
import random
import re

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


def test_add_employee_successfully(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PIMPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # Step 2: Navigate to PIM and click Add
    dashboard_page.navigate_to_pim()
    dashboard_page.click_add_employee()

    # Step 3: Fill details
    emp_id = str(random.randint(10000, 99999))
    # Using absolute path is safer for file uploads
    photo_path = os.path.abspath("assets/my_pic.jpg")

    pim_page.fill_employee_details("Anju", "Tester", emp_id, photo_path)

    # Step 4: Assertions
    assert pim_page.verify_success(), "Success toast message was not displayed!"
    expect(page).to_have_url(   we3re.compile(r".*viewPersonalDetails.*"))