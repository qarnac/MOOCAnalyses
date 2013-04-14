from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "http://www.nasa.gov/multimedia/imagegallery/iotd.html"

# use firefox to get page with javascript generated content
with closing(Firefox()) as driver:
    driver.get(url)
    # get all information using find_element_by_xpath("//*")
    select = driver.find_element_by_xpath("//*")
    source_code = select.get_attribute("outerHTML")
    # save information in this new file
    new_file = open('D:/nasa_source_code.html', 'w')
    new_file.write(source_code.encode('utf-8'))
    new_file.close()

