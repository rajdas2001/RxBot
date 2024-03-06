import google.generativeai as genai
import streamlit as st

#model
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')

#streamlit app
st.title("How can I help you today?")

main_placeholder = st.empty()
query = main_placeholder.text_input("", placeholder="Type here")
main_placeholder_again = st.empty()

#result
if query:
    response = model.generate_content(query).text
    st.write(response)