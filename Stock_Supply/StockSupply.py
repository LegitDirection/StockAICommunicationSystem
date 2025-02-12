import yfinance as yf

from tools.send import Send

def getStockPrice(stockname):
    ticker_symbol = stockname
    stock = yf.Ticker(ticker_symbol)
    info = stock.info

    current_price = info['currentPrice']
    dividend_yeild = info['dividendYield']

    print(f'''
        Stock: {ticker_symbol}, 
        Current price: {current_price}, 
        Dividend yeild: {dividend_yeild}
        ''')

def sendStockData(queue, stockname, dividend_yeild, current_price):
    s1 = Send()
    s1.send_stock_data(queue, stockname, 'bid', dividend_yeild, current_price)


#print(getStockPrice("AAPL"))