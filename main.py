# Imports
import pandas
import streamlit as st


# Functions
def display_project(project):
    st.text("")
    st.image("images/" + project["image"], width=300)
    st.subheader(project["title"])
    st.text(project["description"])
    st.write("[Source Code]({})".format(project["url"]))
    st.text("")


# Configurations
st.set_page_config(layout="wide")

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
        display_project(row)

with project_column_right:
    for index, row in data[half:].iterrows():
        display_project(row)
