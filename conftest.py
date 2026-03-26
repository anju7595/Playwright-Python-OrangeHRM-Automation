import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Check if we are running in GitHub Actions environment
        is_github = os.getenv("GITHUB_ACTIONS") == "true"

        # HEADLESS must be True for GitHub, but can be False for your laptop
        # SLOW_MO is useful for your eyes, but we disable it on GitHub to run faster
        browser = p.chromium.launch(
            headless=is_github,
            slow_mo=0 if is_github else 500
        )

        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()


# This hook handles screenshots on failure (Keep this as is)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get('page')
        if page:
            if not os.path.exists("failures"):
                os.makedirs("failures")

            screenshot_path = f"failures/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n❌ Test Failed! Screenshot saved to: {screenshot_path}")