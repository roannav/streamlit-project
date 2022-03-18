# This is just the tutorial listed below + some notes + some small changes.
# src: tutorial at https://docs.streamlit.io/library/get-started/create-an-app
import streamlit as st
import pandas as pd
import numpy as np

# app title
st.title('Uber pickups in NYC')


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Fetch the Uber dataset for pickups and dropoffs in NYC
# IN: nrows: number of rows to load into the dataframe
# OUT: returns the dataframe
#
# It takes time to download the data.
# Don't reload the data each time the app is updated; instead cache the data
@st.cache
def load_data(nrows):
    # read into a Pandas dataframe
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # convert date column from text to datetime
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using st.cache)')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

#Use NumPy to generate a histogram that breaks down pickup times binned by hour
hist_values = np.histogram( data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# draw it
st.bar_chart(hist_values)


#st.subheader('Map of all pickups')
# draw a map of the area covered in the data
#st.map(data)

#hour_to_filter = 17   # the busiest time, according to the histogram above
#hour_to_filter = 2   # least busiest time, according to the histogram above

# add slider widget
hour_to_filter = st.slider('hour', 0, 23, 17) # min: 0h, max: 23h, default: 17h

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
#st.write(filtered_data)  # show the filtered data in a table
# draw a map of the area covered in the data
st.map(filtered_data)

