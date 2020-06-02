from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

string = input("Type what you want to hear backwards:\n")

# Reverse word and make it lowercase
backwards = string[::-1].lower()

# Open new chrome page
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://translate.google.com/")

# Click English button
english_button = driver.find_element_by_id("sugg-item-en")
english_button.click()

# Type the reversed word
text = driver.find_element_by_id("source")
text.clear()
text.send_keys(backwards)

# Wait for page to load and click listen button
time.sleep(1.5)
listen_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[5]/div')
listen_button.click()


time.sleep(10)
driver.close()

