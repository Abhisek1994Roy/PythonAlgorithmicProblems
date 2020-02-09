import sys
from selenium import webdriver

# Capture the website link passed
argPassed = sys.argv[1]

# Create a headless driver
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path='./chromedriver')

# Get the screenshot of the webpage passed
driver.get('http://' + sys.argv[1])


# Get only the name of the website
nameOfWebSite = argPassed.split(".")[1]

# Use infinite scroll to capture screenshot of entire webpage
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment

# Save the entire webpage
driver.find_element_by_tag_name('body').screenshot(nameOfWebSite+'.png')

driver.quit()
