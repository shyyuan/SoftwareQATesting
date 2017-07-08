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
    element_present1 = EC.presence_of_element_located((By.ID, 'replyhome1'))
    WebDriverWait(driver, timeout).until(element_present1)
    print "Logged in and Home page loaded"
except TimeoutException:
    print "Timed out waiting for home page to load"



currLikes = driver.find_element_by_xpath("/html/body/form/div/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[1]").text
print currLikes + " likes original"

# Like
#driver.find_element_by_css_selector('a.likeLinks > span.glyphicon-heart').click()
driver.find_element_by_id('likehome1').click()


try:
    element_present2 = EC.presence_of_element_located((By.ID, 'replyhome1'))
    WebDriverWait(driver, timeout).until(element_present2)
    print 'Like a post'
except TimeoutException:
    print "Timed out waiting for home page to load"


newLikes = driver.find_element_by_xpath("/html/body/form/div/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[1]").text
print newLikes + " likes now"


# Logout
#driver.find_element_by_link_text('LogOut').click()
driver.find_element_by_xpath("//a[contains(text(),'LogOut')]").click()
print "Log out"


# close the browser window
driver.quit()


print 'Script run successfully'
