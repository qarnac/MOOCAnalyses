import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrape_info(driver):   
    element = driver.find_element_by_xpath("//*[@id='gallery_image_area']/img")
    print "Title : " + element.get_attribute("alt")
    print "URL : " + element.get_attribute("src")     

def simulate_browser(URL):
    driver = webdriver.Firefox()
    driver.get(URL)
    time.sleep(10)
    scrape_info(driver)
    driver.close()
    
if __name__ == "__main__":
    simulate_browser("http://www.nasa.gov//multimedia/imagegallery/iotd.html")
