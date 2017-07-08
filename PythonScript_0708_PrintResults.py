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



# Post 5 posts
for num in range(1,6):

    post = "This is post number " + str(num)
    #print post

    # Post
    driver.find_element_by_id('post').send_keys(post)
    driver.find_element_by_id('submit').submit()

    # wait until the posting is done
    try:
        element_present2 = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.panel-primary > div.panel-body'))
        WebDriverWait(driver, timeout).until(element_present2)
        print "Post a New Post: " + post
    except TimeoutException:
        print "Timed out waiting for new post to load"

print "Posted 5 new post"

allPosts = driver.find_elements_by_xpath("/html/body/form/div/div/div[3]/div[2]/div/div/div[2]")
#driver.find_elements_by_css_selector('div.panel.panel-primary > div.panel-body')
print "Total " + str(len(allPosts)) + " posts:"
# print out the post
for post in allPosts:
    print post.text

#/html/body/form/div/div/div[3]/div[2]/div/div[1]/div[2]
#/html/body/form/div/div/div[3]/div[2]/div/div[2]/div[2]

