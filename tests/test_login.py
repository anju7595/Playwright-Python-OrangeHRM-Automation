import re

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    # Action
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # Assertion (Playwright auto-waits for the URL/Element)
    expect(page).to_have_url(re.compile(r".*/dashboard"))