import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



recipient = sys.argv[1]
subject_line = sys.argv[2]
message = sys.argv[3]

print(recipient, subject_line, message)
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)


driver.get('https://account.proton.me/mail')
time.sleep(5)
driver.find_element(By.ID, "username").send_keys('mwardtestaccount') #email entry

#pword = input('Enter your password here:')
driver.find_element(By.ID, "password").send_keys("code-monkey-pw-fun")
buttons = driver.find_elements(By.TAG_NAME, "button")

print(list(map(lambda b: b.text, buttons)))
buttons[2].click()
# gets list of buttons on the page: print(list(map(lambda b: b.text, pw_entry_buttons)))

time.sleep(10)
logged_in_buttons = driver.find_elements(By.TAG_NAME, "button")
print(list(map(lambda b: b.text, logged_in_buttons)))

for button in logged_in_buttons:
    if button.text == "New message":
        button.click()

driver.find_element(By.CSS_SELECTOR, '[data-testid="composer:to"]').send_keys(recipient)
driver.find_element(By.CSS_SELECTOR, '[data-testid="composer:subject"]').send_keys(subject_line)
ActionChains(driver).key_down(Keys.TAB).send_keys(message).perform()
driver.find_element(By.CSS_SELECTOR, '[data-testid="composer:send-button"]').click()

input('Press enter to close:')

# def test_explicit(driver):
#     driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
#     revealed = driver.find_element(By.ID, "revealed")
#     driver.find_element(By.ID, "reveal").click()

#     wait = WebDriverWait(driver, timeout=2)
#     wait.until(lambda d : revealed.is_displayed())

#     revealed.send_keys("Displayed")
#     assert revealed.get_property("value") == "Displayed"