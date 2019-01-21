from selenium import webdriver
from selenium.webdriver.firefox.options import Options

option = Options()
option.headless = True
browser = webdriver.Firefox(options=option)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
