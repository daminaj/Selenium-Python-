from typing import KeysView
from requests import request
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver1.maximize_window()
driver1.get("https://www.google.com/")