import streamlit as st
from utils import load_email_list
from outlook_handler import fetch_filtered_emails

st.set_page_config(page_title="Outlook Email Filter", layout="wide")
st.title("📨 Outlook Email Filter")

st.sidebar.header("Settings")
max_emails = st.sidebar.slider("Max Emails", 10, 200, 50)

with st.spinner("Loading emails..."):
    email_list = load_email_list()
    emails = fetch_filtered_emails(email_list, max_emails=max_emails)

st.success(f"Found {len(emails)} emails from allowed senders.")

for idx, email in enumerate(emails, 1):
    st.markdown(f"### {idx}. {email['Subject']}")
    st.write(f"**From:** {email['Sender']}  \n**Received:** {email['Received']}")
    with st.expander("Preview"):
        st.text(email['Preview'])
