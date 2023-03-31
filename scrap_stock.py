#!/usr/bin/env python3

import datetime
import sys
import os
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

assert len(sys.argv) > 1, f"ERROR: no file path passed."

data_file = sys.argv[1]

assert os.path.isfile(data_file), f"ERROR: {data_file} is not an existent file."

active_list = []
for i in range(2, len(sys.argv)):
    active_list.append(sys.argv[i])

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)

for active in active_list:
    url = "https://www.tradingview.com/symbols/" + active
    driver.get(url)

    element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, ".last-jXw2qXFy.js-symbol-last"))
    WebDriverWait(driver, 10).until(element_present)

    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    price = soup.find("span", {"class":"last-jXw2qXFy js-symbol-last"}).text
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with(open(data_file, "a")) as f:
        f.write(f"{time_now},{active},{price}\n")

driver.quit()
