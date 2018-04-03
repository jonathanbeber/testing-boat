import os
import time
from selenium import webdriver

host_address = os.environ.get("HOST_ADDRESS", 'localhost')

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
browser = webdriver.Chrome('./chromedriver', options=options)
# Enter the site
browser.get('http://{}:8000'.format(host_address))

# check the site's title
assert 'To-Do' in browser.title

# Insert text 'buy milk' in the new item box

# confirm the action

# Check if the item is in the page

# Insert new item 'Clean the car'

# check if the new item is in the page

# Go to personal URL

# check if 'buy milk' and 'Clean the car' are in a to-do list

# exit
browser.exit()
