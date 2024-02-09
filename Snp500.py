import yfinance as yf
import pandas as pd
from datetime import date



if __name__ == "__main__":
    
    df = pd.read_csv('sp500_stocks.csv')
    # tickers = df['Ticker Symbol'].tolist()
    schema = {}
    tickers = ['AAPL', 'MSFT']
    date = date.today().strftime("%Y-%m-%d")




    for ticker in tickers:
        schema[ticker] = {
            'industry': {'dtype': str},
            'sector': {'dtype': str},
            
        }
        # pd.DataFrame.insert(ticker, date, yf.Ticker(ticker).info['totalCashPerShare'])
        break
    print(pd.DataFrame)