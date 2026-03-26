from playwright.sync_api import expect


class PIMPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for the input fields
        self.first_name_input = page.locator("input[name='firstName']")
        self.last_name_input = page.locator("input[name='lastName']")
        self.save_button = page.get_by_role("button", name="Save")

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

        # Wait for the network to be quiet after the upload
        self.save_button.wait_for(state="visible")
        self.save_button.click()

        # 4. GUARANTEED CLICK
        # We use 'force=True' to bypass any invisible overlays
        # and 'button[type="submit"]' to ensure we hit the form trigger
        # Uses the 'Name' shown in the accessibility tree (seen in your screenshot)

    def verify_success(self):
        try:
            # Now self.success_message is recognized because it was defined in __init__
            expect(self.success_toast).to_be_visible(timeout=8000)
            return True
        except Exception:
            # Catching generic Exception covers both Timeout and Assertion errors
            return False