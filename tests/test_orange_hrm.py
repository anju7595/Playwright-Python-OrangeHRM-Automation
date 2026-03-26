import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_full_user_flow(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # 1. Login
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # 2. Verify Dashboard Loaded
    assert "dashboard" in page.url

    # 3. Navigate to PIM (Personnel Information Management)
    dashboard_page.navigate_to_pim()
    assert "pim/viewEmployeeList" in page.url

    # 4. Logout
    dashboard_page.logout()
    assert "login" in page.url


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("WrongUser", "WrongPass")

    # Verify error message is visible
    error_msg = page.locator(".oxd-alert-content-text")
    expect(page.locator(".oxd-alert-content-text")).to_be_visible()
    assert error_msg.inner_text() == "Invalid credentials"