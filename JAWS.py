from time import time, sleep
from selenium import webdriver
from os import getcwd

script_dir = getcwd()
driver = webdriver.Chrome(script_dir + "/chromedriver")

driver.get("https://techwithtim.net")
sleep(5)
driver.quit()