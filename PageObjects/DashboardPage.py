from selenium.webdriver.common.by import By
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for dashboard page header, My Leave icon, and logout elements
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.my_leave_icon = (By.XPATH, "//p[text()='My Leave']")
        self.user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")

    def is_dashboard_displayed(self):
        # Check if the dashboard header is visible
        try:
            return self.driver.find_element(*self.dashboard_header).is_displayed()
        except:
            return False

    def go_to_my_leave(self):
        # Navigate to the My Leave section
        self.driver.find_element(*self.my_leave_icon).click()

    def logout(self):
        # Perform logout by clicking on dropdown and selecting logout
        self.driver.find_element(*self.user_dropdown).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_link).click()
