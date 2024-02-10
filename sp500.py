import yfinance as yf
import pandas as pd
from datetime import date



if __name__ == "__main__":
    with open ('sp500_stocks.csv', 'r') as f:
        tickers = f.read().splitlines()

        df = pd.DataFrame()
        schema = {}
        date = date.today().strftime("%Y-%m-%d")
        keys = {
            'industry', 
            'industryKey', 
            'industryDisp', 
            'sector', 
            'sectorKey', 
            'sectorDisp', 
            'fullTimeEmployees', 
            'auditRisk', 
            'boardRisk', 
            'compensationRisk', 
            'shareHolderRightsRisk', 
            'overallRisk', 
            'governanceEpochDate', 
            'compensationAsOfEpochDate', 
            'maxAge', 
            'priceHint', 
            'previousClose', 
            'open', 
            'dayLow', 
            'dayHigh', 
            'regularMarketPreviousClose', 
            'regularMarketOpen', 
            'regularMarketDayLow', 
            'regularMarketDayHigh', 
            'dividendRate', 
            'dividendYield', 
            'exDividendDate', 
            'payoutRatio', 
            'fiveYearAvgDividendYield', 
            'beta', 
            'trailingPE', 
            'forwardPE', 
            'volume', 
            'regularMarketVolume', 
            'averageVolume', 
            'averageVolume10days', 
            'averageDailyVolume10Day', 
            'bid', 
            'ask', 
            'bidSize', 
            'askSize', 
            'marketCap', 
            'fiftyTwoWeekLow', 
            'fiftyTwoWeekHigh', 
            'priceToSalesTrailing12Months', 
            'fiftyDayAverage', 
            'twoHundredDayAverage', 
            'trailingAnnualDividendRate', 
            'trailingAnnualDividendYield', 
            'currency', 
            'enterpriseValue', 
            'profitMargins', 
            'floatShares', 
            'sharesOutstanding', 
            'sharesShort', 
            'sharesShortPriorMonth', 
            'sharesShortPreviousMonthDate', 
            'dateShortInterest', 
            'sharesPercentSharesOut', 
            'heldPercentInsiders', 
            'heldPercentInstitutions', 
            'shortRatio', 
            'shortPercentOfFloat', 
            'impliedSharesOutstanding', 
            'bookValue', 
            'priceToBook', 
            'lastFiscalYearEnd', 
            'nextFiscalYearEnd', 
            'mostRecentQuarter', 
            'earningsQuarterlyGrowth', 
            'netIncomeToCommon', 
            'trailingEps', 
            'forwardEps', 
            'pegRatio', 
            'lastSplitFactor', 
            'lastSplitDate', 
            'enterpriseToRevenue', 
            'enterpriseToEbitda', 
            '52WeekChange', 
            'SandP52WeekChange', 
            'lastDividendValue', 
            'lastDividendDate', 
            'exchange', 
            'quoteType', 
            'symbol', 
            'underlyingSymbol', 
            'shortName', 
            'longName', 
            'messageBoardId', 
            'gmtOffSetMilliseconds', 
            'currentPrice', 
            'targetHighPrice', 
            'targetLowPrice', 
            'targetMeanPrice', 
            'targetMedianPrice', 
            'recommendationMean', 
            'recommendationKey', 
            'numberOfAnalystOpinions', 
            'totalCash', 
            'totalCashPerShare', 
            'ebitda', 
            'totalDebt', 
            'quickRatio', 
            'currentRatio', 
            'totalRevenue', 
            'debtToEquity', 
            'revenuePerShare', 
            'returnOnAssets', 
            'returnOnEquity', 
            'freeCashflow', 
            'operatingCashflow', 
            'earningsGrowth', 
            'revenueGrowth', 
            'grossMargins', 
            'ebitdaMargins', 
            'operatingMargins',  
            'trailingPegRatio'
        }
        

        for ticks in tickers:
            for key in keys:
                c = yf.Ticker(ticks).info[key]
                print(c)
                # df.add(yf.Ticker(ticks).info[key])
            # print(ticks)
            # print(f"""
            #       yf.Ticker(ticks).info['industry'], 
            #       """
            #       )
            break
            # print (tickers)

    print(df.head())
    # print(pd.DataFrame.head(df))