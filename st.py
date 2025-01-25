# filepath: hello_world.py
import streamlit as st
from datetime import datetime
st.title('Hello, Vinoth!')
st.write('Welcome to Streamlit!')

# Get the input as calendar date
date = st.date_input('Select a date', datetime.now())

# Display the selected date
st.write('You selected:', date)

