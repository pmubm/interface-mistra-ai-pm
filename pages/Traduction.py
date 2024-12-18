import streamlit as st
from utiles import *
from mistralai import Mistral

api_keys =st.text_imput("apikeys")
client = Mistral(api_keys)
st.title('testtt')

