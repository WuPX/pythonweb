from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8001')
assert 'To-do' in browser.title,"Browse.title was" + browser.title