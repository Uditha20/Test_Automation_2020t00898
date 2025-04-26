from selenium.webdriver.common.by import By

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the leave page header
        self.leave_header = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')

    def is_leave_page_displayed(self):
        # Check if the leave page is displayed
        try:
            return self.driver.find_element(*self.leave_header).is_displayed()
        except:
            return False