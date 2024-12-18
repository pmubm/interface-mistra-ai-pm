import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Entitees')
#ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f
chaine_apik = "ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f"
text_area_api =st.text_input("api_keys",value=chaine_apik)

client = Mistral(text_area_api)
texte_par_defaut = """Bien sûr. Voici une version du texte d'entraînement sans apostrophes, toujours sans chiffres ni guillemets, pour faciliter encore davantage le traitement par un modèle de NER :

Texte d'entraînement (version courte, sans chiffres, guillemets ni apostrophes) :

Emmanuel Macron a rencontré Angela Merkel à Berlin. La discussion portait sur lavenir de lUnion Européenne. Macron sest ensuite rendu à New York pour une session de lAssemblée générale des Nations Unies. Elon Musk dirigeant de Tesla a annoncé une collaboration avec Samsung. Joe Biden président des États-Unis a effectué un voyage à Kyiv. Marie Curie scientifique de renom est née à Varsovie. Albert Einstein a travaillé à Berne. Microsoft fondée par Bill Gates et Paul Allen a lancé une nouvelle version de Windows. Le tournoi de Roland Garros se déroule chaque année à Paris. Narendra Modi Premier ministre de lInde a visité Paris. LOrganisation mondiale de la Santé OMS basée à Genève surveille les épidémies mondiales
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