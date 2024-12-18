import streamlit as st

# Création d'un titre
st.title('Interface-Mistral-AI')

# Création d'un sous-titre
st.subheader("Mistral AI")

# Création d'une zone de texte
st.write("Introduction à mistral AI")


if st.checkbox('Afficher le contenu'):
  st.write("""
  
  # Titre
  ## Sous-titre
  
  **Text**
  
    `print("Hello World")`
  
  """)

# Zone de saisie de texte
user_name = st.text_input("Quel est votre nom ?")

# Création d'un bouton
if st.button("Press OK"):
  st.write(user_name)


# Image
st.sidebar.image('https://i.postimg.cc/JhkNw2FH/istockphoto-1398055471-612x612.jpg')

# Video
st.sidebar.video("https://www.youtube.com/watch?v=14leJ1fg4Pw")

# Cration d'un slider 
user_age = st.slider("Quel est votre age ?", 18, 99, 30)

st.selectbox("Selectionnez votre pays", ["France", "Espagen", "USA"])



# Lecture d'un fichier csv avec pandas
import pandas as pd

path_url = "https://raw.githubusercontent.com/Quera-fr/My-Credit/refs/heads/main/Analyse%20des%20donn%C3%A9es/test.csv"

df = pd.read_csv(path_url)

st.write(df, delimiter=';')