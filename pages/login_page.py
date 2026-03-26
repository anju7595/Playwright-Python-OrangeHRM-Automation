from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()