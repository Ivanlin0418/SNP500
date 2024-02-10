import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import pandas as pd

"""
@Brief: This script is used to scrape the S&P 500 stock symbols from the stockanalysis.com website.
@purpose: Get the ticker symbols of the current companies listed in the snp500. 
@Output: CSV file with the ticker symbols, used in tangent with the sp500.py script to get the stock data.
"""

if __name__ == "__main__":
    URL = "https://stockanalysis.com/list/sp-500-stocks/" ##URL to scrape

    response = requests.get(URL)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    elements = driver.find_elements(By.XPATH, "//td[contains(@class, 'sym') and contains(@class, 'svelte-132bklf')]//a")

    data = [element.text for element in elements]
    df = pd.DataFrame(data, columns=["Ticker Symbol"])

    print (df)
    df.to_csv('sp500_stocks.csv', index=False, headers=False)
    driver.quit()

