import streamlit as st
import math
import numpy as np
import pandas as pd
import datetime
import time
import yfinance as yf

st.title('Simple Market Indices App')
st.text('In this project, I like to display a simple analysis of market indices using this application.')

st.sidebar.header('Welcome to My First App')
name = st.sidebar.text_input('Your Name')
st.sidebar.write(' :) ', name)

option = st.sidebar.selectbox(
    'Market Indices',
     ['Nikkei 225','Dow Jones','Nashdaq 100','S&P 500']
)

if option == 'Nikkei 225':
st.subheader("Nikkei 225")

nikkeidata = pd.read_csv(url = 'https://raw.githubusercontent.com/Aidamia/myfirstapp.py/main/Nikkei%20225.csv')
nikkeiHis = Nikkeidata.history(period='1d', start='2010/1/01', end='2021/11/20')

nikkeidataframe = pd.DataFrame(nikkeidata['Location'].value_counts()).head(50)

    st.write("""## Closing Price""")
    st.line_chart(nikkeiHis.Price)
    st.write("""## Volume Price""")
    st.line_chart(nikkeiHis.Change%)
    
    
    
elif option == 'Dow Jones':
st.subheader("Dow Jones")

dowjonesdata = pd.read_csv(url = 'https://raw.githubusercontent.com/Aidamia/myfirstapp.py/main/Dow%20Jones.csv')
dowjonesHis = dowjonesdata.history(period='1d', start='2010/1/01', end='2021/11/20')

dowjonesdataframe = pd.DataFrame(dowjonesdata['Location'].value_counts()).head(50)

    st.write("""## Closing Price""")
    st.line_chart(dowjonesHis.Price)
    st.write("""## Volume Price""")
    st.line_chart(dowjonesHis.Change%)
    
    
    
elif option == 'Nashdaq 100':
st.subheader("Nashdaq 100")

nashdaq100data = pd.read_csv(url = 'https://raw.githubusercontent.com/Aidamia/myfirstapp.py/main/Dow%20Jones.csv')
nashdaq100His = nashdaq100data.history(period='1d', start='2010/1/01', end='2021/11/20')

nashdaq100dataframe = pd.DataFrame(nashdaq100data['Location'].value_counts()).head(50)

    st.write("""## Closing Price""")
    st.line_chart(nashdaq100His.Price)
    st.write("""## Volume Price""")
    st.line_chart(nashdaq100His.Change%)    
    
    
elif option == 'S&P500':
st.subheader("S&P 500")

sp500data = pd.read_csv(url = 'https://raw.githubusercontent.com/Aidamia/myfirstapp.py/main/Dow%20Jones.csv')
sp500His = sp500data.history(period='1d', start='2010/1/01', end='2021/11/20')

sp500dataframe = pd.DataFrame(sp500data['Location'].value_counts()).head(50)

    st.write("""## Closing Price""")
    st.line_chart(sp500His.Price)
    st.write("""## Volume Price""")
    st.line_chart(sp500His.Change%)        
