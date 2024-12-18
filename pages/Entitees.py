import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Entitees')
#ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f
chaine_apik = "ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f"
text_area_api =st.text_input("api_keys",value=chaine_apik)

client = Mistral(text_area_api)
texte_par_defaut = """Joe Biden, président des États-Unis, a effectué un voyage à Kyiv. Marie Curie, scientifique de renom, est née à Varsovie. Albert Einstein a travaillé à Berne. Microsoft, fondée par Bill Gates et Paul Allen, a lancé une nouvelle version de Windows. Le tournoi de Roland-Garros se déroule chaque année à Paris. Narendra Modi, Premier ministre de l'Inde, a visité Paris. L'Organisation mondiale de la Santé (OMS), basée à Genève, surveille les épidémies mondiales.
"""
# Affiche le contenu actuel de la boîte de texte
prompt = st.text_area("Votre texte :", value=texte_par_defaut)

# Affiche le contenu actuel de la boîte de texte
#st.write("Contenu de la boîte :", texte)



if st.button("Envoyer"):
    response = get_ner(client,prompt)
    
    st.write(response)


    #creer function traduction
    #analyse sentiments
    #creer entité nommée


'''

'''