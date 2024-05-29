from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# This tests the Chrome scraping Driver manager is working correctly
#  working with: python 3.10
#  Load Libraries from repository:
#   Selenium
#   webmanager-driver


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# The install method in the driver make sure any updates to the chrome driver get automatically updated
# It changes alot!!!
driver.get('https://scrapingclub.com')
driver.implicitly_wait(2)
title = driver.title
print("Web Page Title is")
print(title)
driver.close()


