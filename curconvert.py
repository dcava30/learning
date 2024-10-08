import streamlit as st
import time
import requests
from requests import codes

# Title and Leading text

st.title('Currency Converter App')
st.markdown("""
This app converts the value of foreign currencies!
            
Some currency pairs currently do not convert

""")

# Currency price list
currency_list1 = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "MXN", "NZD", "SGD", "HKD", "NOK", "KRW", "TRY", "INR", "RUB", "BRL", "ZAR", "DKK", "PLN", "TDW", "THB", "MYR"]

# Currency converter function

def exchange(f: str, t: str, a: float) -> float:
    if f not in currency_list1 or t not in currency_list1:
        raise ValueError("Invalid currency selection")
    
    params = {
        "from": f,
        "to": t,
        "amount": a,
    }

    headers = {
        "Authorization": "FREE",
    }
    # API request to a private API
    response = requests.get(
        url='https://exchange.nanoapi.dev/api/exchange',
        params=params,
        headers=headers,
        timeout=10
    )

    if response.status_code != codes.ok:
        raise Exception(f"invalid api return code {response.status_code}, this could be a pair that currently doesn't exchange")

    return response.json()["nanoapi"]

# Sidebar and main panel for Converting Currencies from currency list
st.sidebar.header('Currency Options')

amount = st.number_input("Enter amount to convert here")
base_price_unit = st.sidebar.selectbox('Select base currency', currency_list1).upper()
symbols_price_unit = st.sidebar.selectbox('Select target currency', currency_list1).upper()

# Defining the variables for the conversion
a = float(amount)
f = str(base_price_unit)
t = str(symbols_price_unit)


# Convert currency and display - removed progress bar

if st.button("Convert"):
    try:
        res = exchange(f, t, a)
        st.write(f"{amount} {f} = {res} {t}")

    except ValueError as e:
        st.write(e)
        
    except Exception as e:
        st.write(f"An error occurred: {e}")
    
