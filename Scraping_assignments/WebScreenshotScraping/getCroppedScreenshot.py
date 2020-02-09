from selenium import webdriver
from io import BytesIO
from PIL import Image
import sys

# Capture the website link passed
argPassed = sys.argv[1]

# Create a headless driver
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path='./chromedriver')

# Get the screenshot of the webpage passed
driver.get('http://' + argPassed)
screenshot = driver.get_screenshot_as_png();

# Get only the name of the website
nameOfWebSite = argPassed.split(".")[1]

# Set parameters for cropping
left = 0
top = 0
right = 2000
bottom = 2000

im = Image.open(BytesIO(screenshot))
im = im.crop((left, top, right, bottom)) # crop the image
im.save(nameOfWebSite+'.png') # save the new cropped image
driver.quit() # Close the driver once used
