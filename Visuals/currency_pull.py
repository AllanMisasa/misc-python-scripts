import yfinance as yf

tickers = yf.Tickers("GBPDKK=X EURDKK=X DKK=X")

gbphist = tickers.tickers['GBPDKK=X'].history(period="1y")
eurhist = tickers.tickers['EURDKK=X'].history(period="1y")
usdhist = tickers.tickers['DKK=X'].history(period="1y")

latest_gbp =tickers.tickers['GBPDKK=X'].history(period="1d")
latest_eur =tickers.tickers['EURDKK=X'].history(period="1d")
latest_usd =tickers.tickers['DKK=X'].history(period="1d")

#print(usdhist.tail(1)['Close'][0])
#print(latest_usd.tail(1)['Close'][0])

print(usdhist["Close"].values)