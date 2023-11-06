import streamlit as st
import pandas as pd

# Reading the CSV file
df = pd.read_csv('predictions.csv')

# Displaying the data
st.dataframe(df)

# Adding interactive buttons and sliders
if st.button('Refresh Data'):
    st.write('Data refreshed!')

slider = st.slider('Select a range of rows', 0, len(df), (0, 10))
st.dataframe(df[slider[0]:slider[1]])
