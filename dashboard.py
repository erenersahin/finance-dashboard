import streamlit as st
import pandas as pd
import requests
import numpy as np


st.sidebar.title('Options')
option = st.sidebar.selectbox(
    'Which dashboard?',
    ('twitter', 'wallstreetbets', 'stocktwits', 'chart', 'pattern'))

st.title(option)

if option == 'twitter':
    st.header('Twitter Dashboard')
    from twitter_config import *

if option == 'wallstreetbets':
    st.subheader('wallstreetbets')

if option == 'stocktwits':
    stock_symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=6)
    url = f'https://api.stocktwits.com/api/2/streams/symbol/{stock_symbol}.json'
    r = requests.get(url)
    data = r.json()
    for message in data['messages']:
        st.write(message['created_at'])
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])
        st.write(message['body'])
        st.write("---------------------------------------------------")

if option == 'chart':
    st.subheader('chart')

if option == 'pattern':
    st.subheader('pattern')