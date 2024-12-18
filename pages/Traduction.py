import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Traduction')
#ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f
chaine_apik = "ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f"
text_area_api =st.text_input("api_keys",value=chaine_apik)
st.set_page_config('Le titttre')


api_keys = st.secrets("MISTRAL_API")



client = Mistral(text_area_api)
texte_par_defaut = """Le "meilleur" fromage français """
# Affiche le contenu actuel de la boîte de texte
prompt = st.text_area("Votre texte :", value=texte_par_defaut)

# Affiche le contenu actuel de la boîte de texte
#st.write("Contenu de la boîte :", texte)



if st.button("Envoyer"):
    response = get_traduction(client,prompt)
    
    st.write(response)


    #creer function traduction
    #analyse sentiments
    #creer entité nommée


'''

'''