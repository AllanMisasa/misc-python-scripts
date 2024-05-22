import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import time
import matplotlib.animation as animation   
import datetime as dt
import yfinance as yf

tickers = yf.Tickers("GBPDKK=X EURDKK=X DKK=X")

gbphist = tickers.tickers['GBPDKK=X'].history(period="1y")
eurhist = tickers.tickers['EURDKK=X'].history(period="1y")
usdhist = tickers.tickers['DKK=X'].history(period="1y")

latest_gbp =tickers.tickers['GBPDKK=X'].history(period="1d")
latest_eur =tickers.tickers['EURDKK=X'].history(period="1d")


plt.style.use('dark_background')

st.title("Watch USD nosedive")

max_x = len(usdhist["Close"].values)
x = usdhist["Close"].values
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(x)
line.set_ydata(x)
line.set_xdata(np.arange(max_x))

st.header("Realtime plot of USA's downfall")
st_plot = st.pyplot(plt)

def init():  # give a clean slate to start
    line.set_ydata([np.nan] * max_x)

# This function is called periodically
def animate(x):
    latest_usd =tickers.tickers['DKK=X'].history(period="1d")
    latest_usd = latest_usd.tail(1)['Close'][0]
    np.append(x, latest_usd)
    x = np.delete(x, 0)
    # Add x and y to lists
    line.set_ydata(x)
    st_plot.pyplot(plt)

while True:
        # Limit x and y lists to 20 items
    x = x[-max_x:]
    animate(x)
    # sleep for 24 hours
    time.sleep(86400)
