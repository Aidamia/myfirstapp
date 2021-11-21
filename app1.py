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

Nikkeidata = pd.read_csv("https://github.com/Aidamia/myfirstapp/blob/main/Nikkei%20225.csv")
st.subheader('Nikkei 225')
NikkeiHis = Nikkeidata.history(period='1d', start='2010-1-01', end='2021-11-20')

Nikkeidataframe = pd.DataFrame(Nikkeidata['Location'].value_counts()).head(50)

    st.write("""## Closing Price""")
    st.line_chart(NikkeiHis.Price)
    st.write("""## Volume Price""")
    st.line_chart(NikkeiHis.Change%)
    
