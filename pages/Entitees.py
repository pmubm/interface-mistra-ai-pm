import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Entitees')
#ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f
chaine_apik = "ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f"
text_area_api =st.text_input("api_keys",value=chaine_apik)

client = Mistral(text_area_api)
texte_par_defaut = """Le président Emmanuel Macron a rencontré la chancelière Angela Merkel à Berlin le 10 juillet 2021. Cette rencontre, qui s'est déroulée au siège de la Chancellerie fédérale, avait pour objectif de discuter des enjeux européens, notamment la relance économique post-COVID. Macron a ensuite pris un vol pour New York afin de s'adresser à l'Assemblée générale des Nations Unies le 12 juillet.  Plus tard dans le mois, le 27 juillet, Elon Musk, PDG de Tesla, a annoncé un nouveau partenariat avec Samsung pour la production de batteries. En 2022, Joe Biden, le président des États-Unis, a visité Kyiv en Février. Marie Curie, une scientifique renommée, est née à Varsovie le 7 novembre 1867. Albert Einstein a travaillé à l'Office des brevets à Berne au début du XXe siècle. Microsoft, fondé par Bill Gates et Paul Allen, a lancé Windows 11 le 5 octobre 2021. Le tournoi de Roland-Garros s'est déroulé à Paris en mai 2023. Narendra Modi, le Premier ministre de l'Inde, a visité Paris le 14 juillet 2023, jour de la fête nationale française.  L'Organisation mondiale de la Santé (OMS), basée à Genève, continue de surveiller l'évolution de la pandémie. Le 1er janvier 2024, de nouvelles régulations entreront en vigueur.
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