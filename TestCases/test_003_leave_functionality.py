import time
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage

class Test_003_Leave:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_leave_navigation(self):
        # Start browser session
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.base_url)
        time.sleep(5)

        # Login to the system
        login = LoginPage(driver)
        login.login(self.username, self.password)
        time.sleep(5)

        # Navigate to My Leave section
        dashboard = DashboardPage(driver)
        dashboard.go_to_my_leave()
        time.sleep(5)

        # Check if leave page is loaded
        leave = LeavePage(driver)
        if leave.is_leave_page_displayed():
            assert True
            print("Leave page displayed: Test Passed")
        else:
            assert False
            print("Leave page not displayed: Test Failed")

        driver.quit()
