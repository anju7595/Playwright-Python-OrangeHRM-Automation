import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # headless=False lets you see the browser running locally
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()


# This hook runs after every test to check if it passed or failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # we only look at the actual 'call' (the test execution)
    if report.when == "call" and report.failed:
        # Get the 'page' fixture from the test
        page = item.funcargs.get('page')
        if page:
            # Create a folder for failure images if it doesn't exist
            if not os.path.exists("failures"):
                os.makedirs("failures")

            # Save the screenshot using the test name
            screenshot_path = f"failures/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n❌ Test Failed! Screenshot saved to: {screenshot_path}")