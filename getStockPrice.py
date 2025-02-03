import requests
import json

def getStockPrice(stock):
    url = "" + stock
    headers = {'User-Agent': "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data['quoteResponse']['result'][0]['regularMarketPrice']

print(getStockPrice("aapl"))