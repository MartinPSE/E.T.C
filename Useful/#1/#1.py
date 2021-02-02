import streamlit as st
import pandas_datareader as pdr

st.write('''
#삼성전자 주식데이터
마감 가격과 거래량을 차트로 보여주자
''')

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
df = pdr.get_data_yahoo('005930.KS', '2020-01-01', '2020-09-30')

st.line_chart(df.Close)  # 라인차트를 그려보자~
st.line_chart(df.Volume)
