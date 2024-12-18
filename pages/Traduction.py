import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Traduction')

api_keys =st.text_input("api_keys")
client = Mistral(api_keys)

prompt = st.text_area("""
                      
                      
""")

if st.button("Envoyer"):
    response = get_ner(client,prompt)
    
    st.write(response)