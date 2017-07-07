from selenium import webdriver
# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("http://demo.magentocommerce.com/")
# get the search textbox
search_field = driver.find_element_by_css_selector("i.fa.fa-search").click()
driver.find_element_by_id("edit-keys").clear()
# enter search keyword and submit
driver.find_element_by_id("edit-keys").send_keys("phones")
driver.find_element_by_css_selector("div.search-input > button.btn").click()
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
results = driver.find_elements_by_xpath("//*[@class='result-title']/a")
# products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")
# get the number of anchor elements found
print "Found " + str(len(results)) + " products:"
# iterate through each anchor element and print the text that is
# name of the product
for result in results:
    print result.text
# close the browser window
driver.quit()
