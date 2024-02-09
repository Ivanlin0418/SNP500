import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import pandas as pd

if __name__ == "__main__":
    URL = "https://stockanalysis.com/list/sp-500-stocks/"

    response = requests.get(URL)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    elements = driver.find_elements(By.XPATH, "//td[contains(@class, 'sym') and contains(@class, 'svelte-132bklf')]//a")

    data = [element.text for element in elements]
    df = pd.DataFrame(data, columns=["Ticker Symbol"])

    print (df)
    df.to_csv('sp500_stocks.csv', index=False)
    driver.quit()

