import streamlit as st
import os

st.title('interface-mistral-ai-pm')


st.subheader("Mistral AI")


st.write("Introduction à mistral AI")

st.write("""
# Titre

## Sous titre
 `print("Hello World")`
""")

user_name = st.text_input("Quel est votre nom ?")

print(user_name)

os.write('testttt')
os.write(user_name)



# Creation d'un bouton

        
         
