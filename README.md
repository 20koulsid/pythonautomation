<div align="center">
# 🐍 pythonautomation
 
### My personal learning log for Python, Selenium & Pytest — built one topic at a time
 
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-orange?style=for-the-badge)
 
</div>
---
 
## 📖 About
 
This repo is where I practice and document what I'm learning across three areas: **core Python**, **Selenium WebDriver**, and **Pytest**. Each area has its own folder with topic-wise scripts, plus a `PythonProject1` folder reserved for a bigger project once the fundamentals are solid.
 
---
 
## 📑 Table of Contents
 
- [Folder Structure](#-folder-structure)
- [LearningPython](#-learningpython)
- [LearningSelenium](#-learningselenium)
- [LearningPyTest](#-learningpytest)
- [PythonProject1](#-pythonproject1)
- [Getting Started](#-getting-started)
- [Running Tests](#-running-tests)
- [Sample: Pytest Fixtures & Markers](#-sample-pytest-fixtures--markers)
- [Roadmap](#-roadmap)
---
 
## 📂 Folder Structure
 
```
pythonautomation/
│
├── LearningPython/
│   └── (core Python concepts, topic-wise scripts)
│
├── LearningSelenium/
│   └── (Selenium WebDriver concepts, topic-wise scripts)
│
├── LearningPyTest/
│   ├── conftest.py
│   ├── test_additems.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── practice_questions/   # Q1–Q10 combining topics above
│
├── PythonProject1/
│   └── (reserved for a full end-to-end project — coming soon)
│
├── __init__.py
├── .gitattributes
└── README.md
```
 
---
 
## 🔹 LearningPython
 
Core language concepts practiced here:
 
| Topic | Topic | Topic |
|---|---|---|
| Arguments | Built-in functions | Classes & objects |
| Date & time | Exception handling | File I/O |
| String formatting | Lists & modules | Operator precedence |
| String slicing | Strings | Variable scope |
| openpyxl (Excel automation) | Reading `.xls` files | Writing `.xls` files |
| Test data generation | | |
 
---
 
## 🔹 LearningSelenium
 
Selenium WebDriver concepts practiced here:
 
| Topic | Topic | Topic |
|---|---|---|
| Element attributes | Browser commands | Calendars |
| Dropdowns | Multi-select lists | Radio buttons |
| Checkboxes | Auto-suggestion handling | Hidden elements |
| Element enabled checks | Get text of element | Web element & DOM |
| Handling alerts | Handling frames | JavaScript executor |
| List of web elements | Mouse actions | Multi-window handling |
| Screenshots | Sliders | Explicit/implicit waits |
| Selenium + Pytest integration | | |
 
---
 
## 🔹 LearningPyTest
 
Pytest concepts, practiced through a small mock e-commerce test suite (login, logout, cart, add items, checkout):
 
- **Fixtures** — `conftest.py` with an `autouse`, function-scoped `setUp` fixture that wraps every test (`Launch browser → Login → ... → Logoff → Close browser`)
- **Markers** — custom markers like `@pytest.mark.sanity`, plus built-ins `@pytest.mark.skip` and `@pytest.mark.xfail`
- **Assertions** — basic `assert` checks
- **Test organization** — one file per flow: `test_login.py`, `test_logout.py`, `test_cart.py`, `test_additems.py`, `test_checkout.py`
- **Practice questions** — 10 practice problems (`practice_questions/`) combining all of the above
---
 
## 🔹 PythonProject1
 
Reserved for a full, end-to-end automation project once the fundamentals above are complete — not started yet.
 
---
 
## 🚀 Getting Started
 
```bash
# Clone the repo
git clone https://github.com/<your-username>/pythonautomation.git
cd pythonautomation
 
# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
 
# Install dependencies
pip install pytest selenium openpyxl webdriver-manager
```
 
---
 
## 🧪 Running Tests
 
```bash
# Run the full pytest suite
cd LearningPyTest
pytest -v
 
# Run only sanity-marked tests
pytest -m sanity
 
# Run a specific test file
pytest test_login.py
```
 
---
 
## 💡 Sample: Pytest Fixtures & Markers
 
From `LearningPyTest/conftest.py` — an autouse fixture that runs setup/teardown around every test:
 
```python
import pytest
 
@pytest.fixture(scope="function", autouse=True)
def setUp():
    print("Launch browser")
    print("Login successful")
    print("Browse setup")
    yield
    print("Logoff successful")
    print("close browser")
```
 
And from `test_logout.py` — using markers to control test behavior:
 
```python
import pytest
 
@pytest.mark.sanity
def test_logout():
    print("Logout successful")
 
@pytest.mark.skip
def test_calculation1():
    assert 2 * 2 == 8
 
@pytest.mark.xfail
def test_calculation2():
    assert 2 - 2 == 8
```
 
---
 
## 🗺 Roadmap
 
- [ ] Build out `PythonProject1` as a real end-to-end project (e.g. a Page Object Model test suite)
- [ ] Add data-driven tests using `openpyxl`/Excel input
- [ ] Add HTML/Allure test reports for the Pytest suite
- [ ] Add a GitHub Actions CI workflow to run tests on push
<div align="center">
⭐ A living repo — updated as I learn more.
 
</div>
