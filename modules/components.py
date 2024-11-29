import streamlit as st


def page_navigation():
    with st.sidebar:
        st.page_link('main.py', label='Homepage')
        st.page_link('pages/contact.py', label='Contact Me')


def project_card(project):
    st.text("")
    st.image("images/" + project["image"], width=300)
    st.subheader(project["title"])
    st.text(project["description"])
    st.write("[Source Code]({})".format(project["url"]))
    st.text("")
