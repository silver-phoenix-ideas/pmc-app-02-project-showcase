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

intro_html = """
<div style="text-align: center">Below you can find some of the apps 
I've built in Python. Feel free to contact me!</div>
"""

st.text("")
st.html(intro_html)
