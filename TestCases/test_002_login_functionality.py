import time
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage

class Test_002_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login(self):
        # Initialize browser
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.base_url)
        time.sleep(5)

        # Login with provided credentials
        login = LoginPage(driver)
        login.login(self.username, self.password)
        time.sleep(5)

        # Verify dashboard is displayed
        dashboard = DashboardPage(driver)
        if dashboard.is_dashboard_displayed():
            assert True
            print("Dashboard displayed: Test Passed")
        else:
            assert False
            print("Dashboard not displayed: Test Failed")

        driver.quit()