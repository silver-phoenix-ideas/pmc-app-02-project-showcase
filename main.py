# Imports
import pandas
import streamlit as st
import modules.config as config
import modules.components as components

# Configurations
st.set_page_config(layout="wide", page_title="Homepage | " + config.APP_TITLE)
components.page_navigation()

# About Section
about_column_left, about_column_right = st.columns(2)

with about_column_left:
    st.image("images/photo.png")

with about_column_right:
    with open("about.txt") as file:
        about_text = file.read()

    st.subheader("Ardit Sulce")
    st.info(about_text)

# Project Section
intro_html = """
<div style="text-align: center">Below you can find some of the apps 
I've built in Python. Feel free to contact me!</div>
"""

st.text("")
st.html(intro_html)

project_column_left, empty, project_column_right = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")
length = len(data)

if length % 2:
    half = length // 2 + 1
else:
    half = int(length / 2)

with project_column_left:
    for index, row in data[:half].iterrows():
        components.project_card(row)

with project_column_right:
    for index, row in data[half:].iterrows():
        components.project_card(row)
