# import library
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application login page
driver.get("https://navreet.herokuapp.com/")

# to registeration page
driver.find_element_by_xpath('/html/body/form/div/div/div/div/div[2]/div/fieldset/div/a[2]').click()

# wait for the page to load
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'submit'))
    WebDriverWait(driver, timeout).until(element_present)
    print "Registration page loaded"
except TimeoutException:
    print "Timed out waiting for registration page to load"

# find  input fields
nameInput = driver.find_element_by_id("name")
nameInput.clear()
nameInput.send_keys('Sheila')
emailInput = driver.find_element_by_id("email")
emailInput.clear()
emailInput.send_keys('shyyuan@yahoo.com')
passwordInput = driver.find_element_by_id('password')
passwordInput.clear()
passwordInput.send_keys('shyyuan')

driver.find_element_by_id('submit').click()

#
try:
    element_present1 = EC.presence_of_element_located((By.ID, 'submit'))
    WebDriverWait(driver, timeout).until(element_present1)
    print "Home page loaded for new user"
except TimeoutException:
    print "Timed out waiting for Home page to load"




# Post
driver.find_element_by_id('post').send_keys('This is my first post.')
driver.find_element_by_id('submit').submit()

# wait until the posting is done
try:
    element_present2 = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.panel-primary > div.panel-body'))
    WebDriverWait(driver, timeout).until(element_present2)
    print "Post a New Post"
except TimeoutException:
    print "Timed out waiting for new post to load"


# Logout
#driver.find_element_by_link_text('LogOut').click()
driver.find_element_by_xpath('/html/body/form/div/nav/div/ul[2]/li[2]/a').click()
print "Log out"

# close the browser window
driver.quit()

print 'Script run successfully'
