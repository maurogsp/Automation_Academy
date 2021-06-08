from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class MiPrimerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../config/chromedriver')
        # self.driver.get('https://the-internet.herokuapp.com/dropdown')
        # self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        self.driver.get('http://www.uitestingplayground.com/clientdelay')
        self.driver.maximize_window()

    def tearDown(self):
        screenshot = '../screenshots/Screenshot_' + str(time.time()) +'.png'
        self.driver.save_screenshot(screenshot)
        self.driver.close()
        self.driver.quit()

    # def test_chequear_dropdown(self):
    #     dropdown = self.driver.find_element(By.ID,'dropdown')
    #     dropdown_options = Select(dropdown)
    #     dropdown_options.select_by_visible_text('Option 2')
    #     assert dropdown_options.first_selected_option.text == 'Option 2'

    # def test_chequear_alert(self):
    #     alert_button = self.driver.find_element(By.CSS_SELECTOR, 'li > button')
    #     alert_button.click()
    #     alert = Alert(self.driver)
    #     self.assertEqual(alert.text,'I am a JS Alert')
    #     alert.accept()
    #     success_message = self.driver.find_element(By.ID,'result')
    #     self.assertEqual(success_message.text,'You successfully clicked an alert')

    def test_chequear_wait(self):
        button = self.driver.find_element(By.ID,'ajaxButton')
        button.click()
        #self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver,20)
        message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.bg-success')))
        self.assertEqual(message.text,'Data calculated on the client side.')
        print(message.text)


if __name__ == '__main__':
    unittest.main()
