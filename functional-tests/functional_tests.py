import os
import time
from selenium import webdriver

host_address = os.environ.get("HOST_ADDRESS", 'localhost')

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
browser = webdriver.Chrome('./chromedriver', options=options)
browser.get('http://{}:8000'.format(host_address))

assert 'Django' in browser.title
