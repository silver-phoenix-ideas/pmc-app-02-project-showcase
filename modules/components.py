import streamlit as st


def show_page_navigation():
    with st.sidebar:
        st.page_link('main.py', label='Homepage')
        st.page_link('pages/contact.py', label='Contact Me')
