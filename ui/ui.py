import os
import streamlit as st
import requests
from webscraper import scrape_webpage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

st.title("App")

st.sidebar.title("APP")
st.sidebar.write("Add Links:")

website_links = st.sidebar.text_area("Paste Links (One per line)")
upload_button = st.sidebar.button("Upload")
if upload_button:
    if(website_links):
        with st.sidebar:
            with st.spinner("Uploading..."):
                try:
                    scrape_webpage(website_links.split('\n'))
                    st.success("Uploaded!!")
                except ValueError:
                    st.error('Error in url')
    else:
        st.sidebar.error('Empty url value')




if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt:=st.chat_input("What is up?") :
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    #sending to url
    url = f'http://{api_host}:{api_port}/'
    data = {"query": prompt}

    response = requests.post(url, json=data)


    if response.status_code == 200:
        with st.chat_message("assistant"):
            text = response.json()
            response = st.write(text)
        st.session_state.messages.append({"role": "assistant", "content": text})
