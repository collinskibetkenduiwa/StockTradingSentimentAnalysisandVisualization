from  urllib.request import urlopen,Request
from bs4 import BeautifulSoup

news_tables={}

finviz_url='https://finviz.com/quote.ashx?t='
tickers=['AMZN','AMD','FB']


for ticker in tickers:
    url=finviz_url + ticker

    req=Request(url=url, headers={'user-agent':'my-app'})
    response=urlopen(req)

    html= BeautifulSoup(response,'html')
    print(html)
    news_table=html.find(id='news-table')
    news_tables[ticker]=news_table

    break
 

