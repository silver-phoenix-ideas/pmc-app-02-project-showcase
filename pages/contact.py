# Imports
import streamlit as st
import modules.components as components

# Configurations
st.set_page_config(layout="wide", page_title="Contact Me")
components.show_page_navigation()

# Contact Section
st.title("Contact Me")

with st.form(key="contact_form"):
    st.text_input("Your Email Address:")
    st.text_area("Your Message:")
    st.form_submit_button("Send Message")
