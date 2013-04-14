import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# Create a new instance of the FireFox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.google.com")

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("Python")

# submit
inputElement.send_keys(Keys.RETURN)
#or you can use 
#inputElement.submit()

# wait for page to load
time.sleep(5)
# the page is ajaxy so the title is originally this:
print driver.title

# close browser
driver.quit()
