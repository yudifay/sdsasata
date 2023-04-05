from unittest import result
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json


st.title("GSC Submiter by FayBB")
st.write("Hanya web yang sudah terdaftar yang bisa menggunakan tools ini.")


def generate_article(url):
    JSON_KEY_FILE = "fayid.json"
    SCOPES = ["https://www.googleapis.com/auth/indexing"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        JSON_KEY_FILE, scopes=SCOPES)
    http = credentials.authorize(httplib2.Http())
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

    content = {}
    content['url'] = url
    content['type'] = "URL_UPDATED"
    json_ctn = json.dumps(content)
    # print(json_ctn);return
    response, content = http.request(
        ENDPOINT, method="POST", body=json_ctn)
    result = json.loads(content.decode())

    return response

# return "This is a test article generated without any API calls."


url = st.text_input("Masukkan URL Anda.....")
submit_button = st.button(
    label="Submit URL",
    help="Click to Submit URL",
    key="generate_button"
)

if submit_button:
    with st.spinner("Submit URL..."):
        article = generate_article(url)
        if article.status == 200:
            st.write("Sukses Kirim Link:", url)
        else:
            st.write("Website Tidak Terdaftar")
