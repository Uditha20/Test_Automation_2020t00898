import time
from selenium import webdriver

class Test_001_HomePageTitle:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_home_page_title(self):
        # Launch Chrome browser
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.base_url)

        # Wait for page to load
        time.sleep(3)

        # Get page title and close the browser
        act_title = driver.title
        driver.quit()

        # Assert the title is as expected
        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")