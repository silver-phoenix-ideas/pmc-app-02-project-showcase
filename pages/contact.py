# Imports
import streamlit as st
import modules.config as config
import modules.components as components
import modules.email_helper as email_helper

# Configurations
st.set_page_config(layout="wide", page_title="Contact Me | " + config.APP_TITLE)
components.page_navigation()

# Contact Section
st.title("Contact Me")

with st.form(key="contact_form"):
    sender = st.text_input("Your Email Address:")
    message = st.text_area("Your Message:")
    submit = st.form_submit_button("Send Message")

if submit:
    status = st.info("Sending...")
    try:
        email_helper.send_email(sender, message)
        status.info("Your message was sent successfully.")
    except:
        status.error("Your message could not be sent.")
