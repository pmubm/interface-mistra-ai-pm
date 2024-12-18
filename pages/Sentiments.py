import streamlit as st
from utiles import *
from mistralai import Mistral

st.title('Entitees')
#ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f
api_keys =st.text_input("api_keys")
client = Mistral(api_keys)

prompt = st.text_area("""
                      
                      
""")

if st.button("Envoyer"):
    response = get_ner(client,prompt)
    
    st.write(response)


    #creer function traduction
    #analyse sentiments
    #creer entité nommée


'''
Le "meilleur" fromage français est une question subjective qui dépend des goûts personnels de chacun. La France est célèbre pour sa grande variété de fromages, chacun ayant ses propres caractéristiques uniques en termes de texture, de saveur et de méthode de fabrication. Voici quelques fromages français très appréciés parmi les amateurs de fromage :

1. **Camembert de Normandie** : Un fromage à pâte molle et à croûte fleurie, originaire de Normandie, avec une texture crémeuse et une saveur douce mais complexe.
2. **Roquefort** : Un fromage persillé (à pâte bleue) fabriqué à partir de lait de brebis, avec une saveur forte et piquante.
3. **Brie de Meaux** : Un fromage à pâte molle et à croûte fleurie, originaire de la région de Meaux, avec une texture crémeuse et une saveur douce.
4. **Comté** : Un fromage à pâte pressée cuite, originaire de la région du Jura, avec une texture ferme et une saveur riche et complexe.
5. **Reblochon** : Un fromage à pâte pressée non cuite, originaire de la Savoie, avec une texture crémeuse et une saveur douce et fruitée.
6. **Chèvre (Crottin de Chavignol)** : Un fromage de chèvre, souvent consommé en jeune (fraîche) ou affiné, avec une texture friable et une saveur délicate.
7. **Munster** : Un fromage à pâte molle et à croûte lavée, originaire des Vosges, avec une texture crémeuse et une saveur forte et aromatique.
8. **Époisses** : Un fromage à pâte molle et à croûte lavée, originaire de Bourgogne, avec une texture crémeuse et une saveur forte et épicée.

Chacun de ces fromages a ses propres qualités et peut être considéré comme le "meilleur" en fonction des préférences individuelles. La diversité des fromages français permet de satisfaire une grande variété de goûts et de palais.
'''