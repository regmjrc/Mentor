#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:03:51 2023

@author: johncounsell
"""

import pandas as pd
import streamlit as st

df = pd.read_excel('Mentor_database.xlsx')

# Define the Streamlit app
st.title("DSIS Mentor Identification App")

st.markdown('**This app allows you to filter all staff in DSIS to identify colleagues with the appropriate background to potentially act as your mentor.**')
st.markdown('**Please use the boxes below to filter names as requested. You can use the links to staff Iris pages to find out more about their background.**')
st.markdown('**Once you have identified potential mentors, email them to enquire whether they are open to offering mentorship**')

# Create a dictionary to store the selected options for each menu
selected_options = {}

# Create a list of columns to use as selectbox options
columns = ['Department', 'Discipline', 'Career stage']

# Loop over the columns and create a selectbox for each one
for col in columns:
    # Create a list of options for the selectbox
    options = ['Any'] + list(df[col].unique())
    
    # Display the selectbox and store the selected option in the dictionary
    selected_options[col] = st.selectbox(f"Select an option for {col}", options)

# Filter the DataFrame based on the selected options
filtered_df = df
for col, option in selected_options.items():
    if option != 'Any':
        filtered_df = filtered_df[filtered_df[col] == option]

columns_to_hide = ["Department", "Discipline", "Role", "Career stage"]
filtered_df = filtered_df.drop(columns_to_hide, axis=1)
filtered_df['Email'] = filtered_df['Email'].apply(lambda x: '<a href="mailto:{}">{}</a>'.format(x, x))

st.write(filtered_df.to_html(escape=False, index=False), unsafe_allow_html=True)
