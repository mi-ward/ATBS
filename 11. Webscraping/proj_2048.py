import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import TimeoutException

t = time.time()
driver = webdriver.Firefox()

driver.set_page_load_timeout(5)

try:
    driver.get('https://gabrielecirulli.github.io/2048/')
except TimeoutException:
    driver.execute_script("window.stop();")

#click new game, say ok?

#click tile inner

ActionBuilder(driver).clear_actions()

def tryAgain():
    try_again_element = driver.find_element(By.CLASS_NAME, "retry-button")
    return (len(try_again_element.text) == 0)


while tryAgain():
    driver.find_element(By.CLASS_NAME, 'game-container').click()
    ActionChains(driver).key_down(Keys.ARROW_UP).perform()
    ActionChains(driver).key_down(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    ActionChains(driver).key_down(Keys.ARROW_LEFT).perform()

input("Press Enter to exit.")
driver.close()
