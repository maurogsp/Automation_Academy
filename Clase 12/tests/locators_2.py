from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


class MiPrimerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../config/chromedriver')
        self.driver.get('https://todomvc.com/examples/vanillajs/')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_crear_nota(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('Soy una notita')
        search_input.send_keys(Keys.ENTER)
        first_note_text = self.driver.find_element_by_css_selector('.view > label')
        assert first_note_text.text == 'Soy una notita'

    def test_crear_dos_notas(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('Soy una notita')
        search_input.send_keys(Keys.ENTER)
        search_input.click()
        search_input.send_keys('Soy otra notita')
        search_input.send_keys(Keys.ENTER)
        # first_note_text = self.driver.find_element_by_css_selector('.view > label')
        # assert first_note_text.text == 'Soy una notita'
        # second_note_text = self.driver.find_element_by_css_selector('.view > label')
        # assert second_note_text.text == 'Soy otra notita'
        notes = self.driver.find_elements(By.CSS_SELECTOR,'.todo-list  .view')
        assert notes[0].text == 'Soy una notita'
        assert notes[1].text == 'Soy otra notita'


if __name__ == '__main__':
    unittest.main()
