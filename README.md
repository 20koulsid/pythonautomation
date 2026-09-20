<div align="center">
# 🐍 Python Automation Playground
 
### Hands-on notes, scripts & projects from learning Python Automation, Selenium & Pytest
 
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.x-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Learning-orange?style=for-the-badge)
 
</div>
---
 
## 📖 About
 
This repository is a personal knowledge base built while learning **Python automation**, **Selenium WebDriver**, and **Pytest**. It contains code snippets, mini-projects, and exercises organized by topic — useful both as a learning log and a quick-reference cheat sheet.
 
---
 
## 📑 Table of Contents
 
- [About](#-about)
- [Tech Stack](#-tech-stack)
- [Folder Structure](#-folder-structure)
- [Topics Covered](#-topics-covered)
- [Getting Started](#-getting-started)
- [Running Tests](#-running-tests)
- [Sample Snippet](#-sample-snippet)
- [Roadmap](#-roadmap)
- [Resources](#-resources)
- [License](#-license)
---
 
## 🛠 Tech Stack
 
| Category      | Tools / Libraries              |
|----------------|--------------------------------|
| Language       | Python 3.10+                   |
| Automation     | Selenium WebDriver             |
| Testing        | Pytest, pytest-html, pytest-xdist |
| Env Management | venv / pip                     |
| Browser Driver | webdriver-manager              |
| Version Control| Git & GitHub                   |
 
---
 
## 📂 Folder Structure
 
```
python-automation-playground/
│
├── selenium_basics/
│   ├── 01_open_browser.py
│   ├── 02_locators.py
│   └── 03_forms_and_waits.py
│
├── pytest_basics/
│   ├── test_fixtures.py
│   ├── test_parametrize.py
│   └── test_markers.py
│
├── projects/
│   └── login_automation_suite/
│
├── utils/
│   └── helpers.py
│
├── requirements.txt
└── README.md
```
 
---
 
## ✅ Topics Covered
 
### 🔹 Python Automation
- [x] File & folder automation
- [x] Working with `os`, `shutil`, `pathlib`
- [x] Scheduling scripts (`schedule`, `cron`)
- [x] Sending automated emails/reports
### 🔹 Selenium
- [x] Browser setup & WebDriver basics
- [x] Locator strategies (`id`, `xpath`, `css selector`)
- [x] Explicit vs Implicit waits
- [x] Handling forms, dropdowns, alerts
- [x] Page Object Model (POM)
### 🔹 Pytest
- [x] Test discovery & naming conventions
- [x] Fixtures & `conftest.py`
- [x] Parametrized tests
- [x] Markers & custom markers
- [x] HTML/Allure test reports
---
 
## 🚀 Getting Started
 
```bash
# Clone the repo
git clone https://github.com/<your-username>/python-automation-playground.git
cd python-automation-playground
 
# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
 
# Install dependencies
pip install -r requirements.txt
```
 
---
 
## 🧪 Running Tests
 
```bash
# Run all tests
pytest
 
# Run with verbose output
pytest -v
 
# Run a specific test file
pytest pytest_basics/test_fixtures.py
 
# Generate an HTML report
pytest --html=report.html
```
 
---
 
## 💡 Sample Snippet
 
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
 
driver = webdriver.Chrome()
driver.get("https://example.com")
 
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)
 
driver.quit()
```
 
---
 
## 🗺 Roadmap
 
- [ ] Add Page Object Model project (real-world login flow)
- [ ] Integrate Allure reporting
- [ ] Add CI pipeline with GitHub Actions
- [ ] Add data-driven testing examples
---
 
## 📚 Resources
 
- [Selenium Docs](https://www.selenium.dev/documentation/)
- [Pytest Docs](https://docs.pytest.org/)
- [Real Python – Automation](https://realpython.com/)
---
 
## 📄 License
 
This project is licensed under the [MIT License](LICENSE).
 
<div align="center">
⭐ If this helped you, consider giving the repo a star!
 
</div>


