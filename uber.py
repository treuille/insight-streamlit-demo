import streamlit as st
import pandas as pd
import numpy as np

DATE_TIME = 'date/time'
DATA_URL = '/Users/adrien/Downloads/uber-raw-data-sep14.csv.gz'

@st.cache
def load_data(nrows):
    """Load the Uber NYC pickup dataset for 9/14."""
    with st.spinner('Loading data...'):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
        return data

# Display the title
st.header('Streamlit for Insight')
st.write("""
_This script demonstrates viewing and manipulating some Uber data using Streamlit._
- For help, please ask the [support channel](https://community.insightdata.com/community/channels/streamlit_support), check the [docs](http://streamlit.io/docs), or just run `streamlit help` from the command line.
- For the source code, click [here](https://github.com/treuille/insight-streamlit-demo).
""")

# Load the data.
data = load_data(100001)

# Filter the data by hour.
hour = 18
data = data[data[DATE_TIME].dt.hour == hour]

# Display the raw data.
st.subheader('Raw Data at %d:00' % hour)
st.write(data)

# Display a histogram of the data.
st.subheader('Usage By Minute at %d:00' % hour)
st.bar_chart(np.histogram(data[DATE_TIME].dt.minute, bins=60, range=(0,60))[0])
