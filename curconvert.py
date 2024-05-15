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
currency_list =  [
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BRL",
            "BSD",
            "BTC",
            "BTN",
            "BWP",
            "BYN",
            "BYR",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLF",
            "CLP",
            "CNH",
            "CNY",
            "COP",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
            "GGP",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "IMP",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JEP",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRO",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SLL",
            "SOS",
            "SRD",
            "SSP",
            "STD",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "UYU",
            "UZS",
            "VEF",
            "VES",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XAG",
            "XAU",
            "XCD",
            "XDR",
            "XOF",
            "XPD",
            "XPF",
            "XPT",
            "YER",
            "ZAR",
            "ZMW",
            "ZWL"
        ]

# Currency converter function

def exchange(f: str, t: str, a: float) -> float:
    if f not in currency_list or t not in currency_list:
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
        raise Exception(f"invalid api return code {response.status_code}")

    return response.json()["nanoapi"]

# Sidebar and main panel for Converting Currencies from currency list
st.sidebar.header('Currency Options')

amount = st.number_input("Enter amount to convert here")
base_price_unit = st.sidebar.selectbox('Select base currency', currency_list).upper()
symbols_price_unit = st.sidebar.selectbox('Select target currency', currency_list).upper()

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
    