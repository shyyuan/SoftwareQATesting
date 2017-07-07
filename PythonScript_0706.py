# import library
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

timeoutMsg = "Timed out waiting for page to load"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application login page
driver.get("https://navreet.herokuapp.com/")
# login page
# find username and password input fields
userNameInput = driver.find_element_by_id('email')
userNameInput.clear()
userNameInput.send_keys('Student')
passwordInput = driver.find_element_by_id('password')
passwordInput.clear()
passwordInput.send_keys('abc123')
# click login button
loginBtn = driver.find_element_by_id('login')
loginBtn.click()
# submit has the same function in this case
#loginBtn.submit()

# wait for the page to load
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'replyhome1'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Timed out waiting for home page to load"


# Post
driver.find_element_by_id('post').send_keys('This is a post testing')
driver.find_element_by_id('submit').submit()

# wait until the posting is done
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.panel-heading > div.panel-body'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Timed out waiting for new post to load"

# Like
#driver.find_element_by_css_selector('a.likeLinks > span.glyphicon-heart').click()
driver.find_element_by_id('likehome1').click()

# Reply
driver.find_element_by_id('replyhome1').click()
driver.find_element_by_id('replyContenet1').send_keys('Today is a nice day')
driver.find_element_by_id('repEnterhome1').click()

# confirm the reply is there

# Logout
driver.find_element_by_link_text('LogOut').click()
driver.find_element_by_xpath('/html/body/form/div/nav/div/ul[2]/li[2]/a').click()



# close the browser window
#driver.quit()
