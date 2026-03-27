# OrangeHRM Playwright-Python Automation Framework

This repository contains a professional-grade test automation framework built with Python, Playwright, and Pytest. It follows the Page Object Model (POM) design pattern to ensure scalability, maintainability, and clean code.

🚀 Features
* Page Object Model (POM): Separates test logic from UI locators.

* Data-Driven Testing: Uses pytest.mark.parametrize and JSON to run multiple test cases efficiently.

* Web-First Assertions: Implements Playwright's auto-retrying expect to handle asynchronous redirects.

* Modular Package Structure: Organized with __init__.py files for professional namespace management.

* Dynamic Waits: Utilizes networkidle and explicit timeouts to handle heavy ERP latency.

**🛠️ Tech Stack**
* Language: Python 3.x

*Automation Tool : Playwright

* Test Runner: Pytest

* IDE: PyCharm

* Version Control: Git
* Reporting	 : Allure Report
* CI/CD :	GitHub Actions
* Pattern :	Page Object Model (POM)

**📂 Project Structure**
Plaintext
OrangeHRM_Playwright_Automation/
├── data/                # Test data (JSON files)
├── pages/               # Page Object classes (UI Locators & Actions)
├── tests/               # Test scripts (Test Workflows)
├── conftest.py          # Browser fixtures and global setup
├── pytest.ini           # Pytest configuration
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation




⚙️ Setup & Installation
1. Clone the repository:

git clone <your-repo-url>
cd OrangeHRM_Playwright_Automation

2. Create a virtual environment:

python -m venv venv source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt
playwright install chromium

🏃 **Running Tests**
* Run all tests (Headless): pytest

* Run with Browser (Headed): pytest --headed

* Run with Tracing: pytest --tracing on

# 📊 Live Automation Dashboard
View the latest automated test execution results and history here:
👉 [Interactive Allure Report](https://anju7595.github.io/Playwright-Python-OrangeHRM-Automation/)

---