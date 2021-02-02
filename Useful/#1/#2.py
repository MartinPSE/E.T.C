import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px


st.write('# 비트코인 BTC 데이터')

# https://coinmarketcap.com
scraper = CmcScraper('BTC', '01-01-2021', '07-01-2021') # %d-%m-%Y' // CmcScraper 사용할 때 는 날짜를 거꾸로 사용해줘야한다.


df = scraper.get_dataframe()

fig_close = px.line(df, x='Date', y= ['Open', 'High', 'Low', 'Close'] , title = "가격")
fig_volume = px.line(df,x='Date', y=['Volume'], title='거래량')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)

# cd 로 경로 변경 해주기~