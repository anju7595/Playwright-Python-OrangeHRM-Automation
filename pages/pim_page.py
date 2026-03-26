from playwright.sync_api import Page, expect  # <-- import Page here

class PIMPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for the input fields
        self.first_name_input = page.locator("input[name='firstName']")
        self.last_name_input = page.locator("input[name='lastName']")
        self.save_button = page.get_by_role("button", name="Save")
        # Success toast/message after saving
        self.success_toast = page.locator("div.orangehrm-toast")  # adjust selector

    def enter_first_name(self, fname):
        self.first_name_input.fill(fname)

    def enter_last_name(self, lname):
        self.last_name_input.fill(lname)

    def click_save(self):
        self.save_button.click()

    def fill_employee_details(self, first_name, last_name, emp_id, photo_path):
        # 1. Fill Names
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)

        # 2. Fill Employee ID
        self.page.locator("div.oxd-input-group:has-text('Employee Id') input").fill(emp_id)

        # 3. Upload Photo
        self.page.locator("input[type='file']").set_input_files(photo_path)

        # Wait for save button to be visible and click
        self.save_button.wait_for(state="visible")
        self.save_button.click()

    def verify_success(self):
        try:
            expect(self.success_toast).to_be_visible(timeout=8000)
            return True
        except Exception:
            return False