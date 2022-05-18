from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = 'C:\Program Files (x86)/chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.pizzahut.com')

sign_in = driver.find_element(By.CLASS_NAME,'jss28')
sign_in.click()


time.sleep(3)
captcha = driver.find_element(By.CLASS_NAME,'recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox')
captcha.click()










# link = driver.find_element(By.LINK_TEXT,'Pizza')
# link.click()

# time.sleep(3)
# link = driver.find_element(By.LINK_TEXT,'Order Now')
# link.click()

# time.sleep(3)
# link = driver.find_element(By.ID,'find-occasion-carryout')
# link.click()

# time.sleep(2)
# search = driver.find_element(By.ID,'zip-input')
# search.send_keys('91360')
# search.send_keys(Keys.RETURN)

