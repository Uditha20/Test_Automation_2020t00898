from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Define locators for username, password and login button
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

    def set_username(self, username):
        # Input username into username field
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        # Input password into password field
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        # Click the login button
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        # Perform login by filling credentials and clicking login
        self.set_username(username)
        self.set_password(password)
        self.click_login()