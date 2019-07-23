from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8001')
assert 'Django' in browser.title