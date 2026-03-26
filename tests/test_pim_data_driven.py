import re

import pytest
import json
import os

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


# Helper function to load data from the JSON file
def load_test_data():
    # Using os.path ensures it works regardless of where you run pytest from
    file_path = os.path.join(os.path.dirname(__file__), '../assets/employees.json')
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.mark.parametrize("user", load_test_data())
def test_add_employee_json(page, user):
    # Initialize Page Objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PIMPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # Step 2: Navigate to PIM and click Add
    dashboard_page.navigate_to_pim()
    dashboard_page.click_add_employee()

    # Step 3: Fill details using the JSON data
    # Ensure these methods (enter_first_name, enter_last_name) exist in your PIMPage
    pim_page.enter_first_name(user['fname'])
    pim_page.enter_last_name(user['lname'])

    # Step 4: Click Save (The method we just discussed!)
    pim_page.click_save()

    # Step 5: Assertion
    # Verify we moved to the Personal Details page for the specific user
    expect(page).to_have_url(
        re.compile(r".*/viewPersonalDetails/.*"),
        timeout=15000)
    print(f"Successfully added employee: {user['fname']} {user['lname']}")