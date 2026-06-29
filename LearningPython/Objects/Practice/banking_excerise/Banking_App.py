# 1. BasePage
# wait_for_element(locator)
# click(locator)
class BasePage:
    def __init__(self,driver):
        self.driver = driver
    def open_url(self,url):
        self.driver.get(url)
        # driver → local variable (comes from outside)
        # self.driver → class-level variable (stored inside the object)
        # So we are saving the driver inside the class instance

    def click(self,locator):
        self.driver.find_element(*locator).click()
# 2. LoginPage
# enter_customer_id()
# enter_pin()
# submit_login()
# login() → return AccountPage
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def user_name(self,username):
        print(f"typing username {username}")
    def password(self,password):
        print(f"typing password {password}")
    def login(self):
        self.login()

# 3. AccountPage
# check_balance()
# deposit(amount)
# withdraw(amount)
# logout()