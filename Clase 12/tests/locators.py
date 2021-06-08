from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

driver = webdriver.Chrome('../config/chromedriver')
driver.get('https://todomvc.com/examples/vanillajs/')

search_input = driver.find_element_by_css_selector('.new-todo')
search_input.click()
search_input.send_keys('soy una notita')
search_input.send_keys(Keys.ENTER)

search_input.click()
search_input.send_keys('soy otra notita')
search_input.send_keys(Keys.ENTER)

#first_note = driver.find_element(By.CSS_SELECTOR,'.todo-list  .view')
#first_note_check = first_note.find_element(By.CSS_SELECTOR,'.toggle')

notes = driver.find_elements(By.CSS_SELECTOR,'.todo-list  .view')

# first_note_check = notes[0].find_element(By.CSS_SELECTOR,'.toggle')
# second_note_check = notes[1].find_element(By.CSS_SELECTOR,'.toggle')
# first_note_check.click()
# second_note_check.click()

for elem in notes:
    elem.find_element(By.CSS_SELECTOR,'.toggle').click()

# toggle_all_btn = driver.find_element(By.ID, 'toggle-all')
# toggle_all_btn.click()


if __name__ == '__main__':
    unittest.main()
