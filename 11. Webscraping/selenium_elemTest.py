from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'jumbotron')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except Exception as excpt:
    print(excpt)
    print('Was not able to find an element with that name.')