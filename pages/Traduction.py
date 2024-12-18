import streamlit as st
from utiles import *
from mistralai import Mistral

api_keys =st.text_imput("api_keys")
client = Mistral(api_keys)

prompt = st.test_area("""
                      
                      
""")

response = get_ner(client,prompt)

st.title('Traduction')

