#Description: This is a stock market dashboard to show more charts and data on some of my portfolio

#Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image


#Add a title and an image
st.write("""
#Stock Market web application 
**Visually** show data on a stock! Date Range from Jan 19, 2021 - Jan 19 2022
""")

image = Image.open("/j.powell.jpg")
st.image(image, use_column_width=True)
st.sidebar.header('User Input')

#Create a function to get the users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2021-01-19")
    end_date = st.sidebar.text_input("Start Date", "2022-01-19")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

#Create a function to  get the company name

def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'TATASTEEL.NS':
        return "Tata Steel"
    elif symbol == 'GOOG':
        return 'Alphabet'
    elif symbol == 'MSFT':
        return 'Microsoft'
    elif symbol == 'NVDA':
        return 'Nvidia'
    else:
        'None'

#timeframe and data
def get_data(symbol, start, end):
    if symbol.upper()== 'AMZN':
        df = pd.read_csv("/stocks/AMZN.csv")
    elif symbol.upper()== 'GOOG':
        df = pd.read_csv("/stocks/GOOG.csv")
    elif symbol.upper()== 'MSFT':
        df = pd.read_csv("/stocks/MSFT.csv")
    elif symbol.upper()== 'NVDA':
        df = pd.read_csv("/stocks/NVDA.csv")
    elif symbol.upper()== 'TATASTEEL.NS':
        df = pd.read_csv("/stocks/TATASTEEL.NS.csv")
    else:
        df = pd.DataFrame(columns = ['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])


    #Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #set the start and end index rows both to 0

    start_row = 0
    end_row = 0
        #Start the date from the top of the data set and go down to see if the users start date is less than or equal to the date in the dataset
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break


    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break
    # Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

#Get the users input
start, end, symbol = get_input()
#get the data
df = get_data(symbol, start, end)
#get the company name
company_name = get_company_name(symbol.upper())

#Display the close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

#Display the close Volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

#Get statistics on the data
st.header('Data Statistics')
st.write(df.describe())



