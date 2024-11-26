import streamlit as st

st.set_page_config(layout="wide")

column_left, column_right = st.columns(2)

with column_left:
    st.image("images/photo.png")

with column_right:
    with open("about.txt") as file:
        about_text = file.read()

    st.subheader("Ardit Sulce")
    st.info(about_text)
