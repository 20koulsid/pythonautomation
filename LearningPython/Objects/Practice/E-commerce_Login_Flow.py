# 1. BasePage
# open_url(url)
# click(locator)
# send_keys(locator, value)
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def open_url(self,url):
        self.driver.get(url) # opens a website and if we use return url it will return url only
    def click_login(self):
        self.driver.find_element(By.ID, "login_button").click()


# 2. LoginPage
# enter_email(email)
# enter_password(password)
# click_login()
# login(email, password) → return HomePage
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def user_name(self,username):
        print(f"typing the username {username}")
    def enter_password(self,password):
        print(f"typing the password {password}")
    def click_login(self):
        print(f"clicking login button")
        print("Loggedin successfully")
        return HomePage
# 3. HomePage
# get_welcome_text()
# search_product(product_name)
# logout()
class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    # locators
    WELCOME_TEXT = (By.ID,"welcome_text")
    SEARCH_BOX = (By.CSS_SELECTOR,"search_box")
    SEARCH_PRODUCT = (By.XPATH,"//*[@id='search_product']")
    LOGIN_BUTTON = (BY.CLASS_NAME,"login_button")
    def get_welcome_text(self):
        return self.driver.find_element(*self.WELCOME_TEXT).text
    def get_search_product(self):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

def get_login_button(self):
        return self.driver.find_element(*self.LOGIN_BUTTON).click()



