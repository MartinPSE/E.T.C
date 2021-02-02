import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime

st.write('# Cryptocurrency Web App')

st.sidebar.header('Menu')  # sidebar를 만들어주자

name = st.sidebar.selectbox('Name',['BTC','ETH','USDT']) # 코인의 종류 선택해줘 !

start_date = st.sidebar.date_input('Start date',datetime(2021,1,1))
end_date = st.sidebar.date_input('End data', datetime(2021,2,3))

# https://coinmarketcap.com
scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))  # 월 -> 일 -> 년

df =scraper.get_dataframe()

fig_close = px.line(df,x='Date' , y=['Open', 'High' ,'Low', 'Close'], title = 'Price')
fig_volume = px.line(df, x = 'Date' , y=['Volume'] , title = 'Volume')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)

