import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Entitees')
#ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f
chaine_apik = "ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f"
text_area_api =st.text_input("api_keys",value=chaine_apik)

client = Mistral(text_area_api)
texte_par_defaut = """
Plus tard dans le mois, le 27 juillet, Elon Musk, PDG de Tesla, a annoncé un nouveau partenariat avec Samsung pour la production de batteries. En 2022, Joe Biden, le président des États-Unis, a visité Kyiv en Février. Marie Curie, une scientifique renommée, est née à Varsovie le 7 novembre 1867. Albert Einstein a travaillé à l'Office des brevets à Berne au début du XXe siècle.
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