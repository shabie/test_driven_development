from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--headless')

browser = webdriver.Chrome(desired_capabilities=chromeOptions.to_capabilities())
browser.get('http://localhost:8000')

try:
    assert 'Django' in browser.title
finally:
    browser.close()