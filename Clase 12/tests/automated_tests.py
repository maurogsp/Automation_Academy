from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class MiPrimerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../config/chromedriver')
        self.driver.get('https://todomvc.com/examples/vanillajs/')
        self.driver.maximize_window()

    def tearDown(self):
        screenshot = '../screenshots/Screenshot_' + str(time.time()) +'.png'
        self.driver.save_screenshot(screenshot)
        self.driver.close()
        self.driver.quit()

    def test_1(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('Nota 1')
        search_input.send_keys(Keys.ENTER)
        search_input.click()
        search_input.send_keys('Nota 2')
        search_input.send_keys(Keys.ENTER)
        search_input.click()
        search_input.send_keys('Nota 3')
        search_input.send_keys(Keys.ENTER)
        search_input.click()
        search_input.send_keys('Nota 4')
        search_input.send_keys(Keys.ENTER)
        notes = self.driver.find_elements(By.CSS_SELECTOR,'.todo-list  .view')
        notes[2].find_element(By.CSS_SELECTOR,'.toggle')
        notes[3].find_element(By.CSS_SELECTOR,'.toggle')
        self.assertEqual(notes[0].text, 'Nota 1')
        self.assertEqual(notes[1].text, 'Nota 2')
        active_notes_button = self.driver.find_element_by_css_selector('body > section > footer > ul > li:nth-child(2) > a')
        active_notes_button.click()
        notes_active = self.driver.find_elements(By.CSS_SELECTOR,'.todo-list  .view')
        self.assertEqual(notes_active[0].text, 'Nota 1')
        self.assertEqual(notes_active[1].text, 'Nota 2')
        #assert active_notes_button.text == 'Active'


if __name__ == '__main__':
    unittest.main()
