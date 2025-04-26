import time
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage

class Test_004_Logout:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_logout(self):
        # Launch the browser and login
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.base_url)
        time.sleep(2)

        login = LoginPage(driver)
        login.login(self.username, self.password)
        time.sleep(3)

        # Perform logout
        dashboard = DashboardPage(driver)
        dashboard.logout()
        time.sleep(2)

        # Verify if logout was successful (URL contains 'login')
        current_url = driver.current_url
        if "login" in current_url:
            assert True
            print("Logout successful: Test Passed")
        else:
            assert False
            print("Logout failed: Test Failed")

