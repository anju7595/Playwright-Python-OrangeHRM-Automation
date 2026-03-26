class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-name")
        self.logout_link = page.get_by_role("menuitem", name="Logout")
        self.pim_menu = page.get_by_role("link", name="PIM")

    def logout(self):
        self.user_dropdown.click()
        self.logout_link.click()

    def navigate_to_pim(self):
        self.pim_menu.click()

    def click_add_employee(self):
        self.page.get_by_role("button", name=" Add").click()