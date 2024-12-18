import streamlit as st
import pandas as pd  # Ajouter pandas pour gérer le CSV
from utiles import get_ner, get_agent_response, get_agent_sentiment_response, get_agent_scrum_response
from mistralai import Mistral



client = Mistral(api_key="ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])







# side bar select
selection = st.sidebar.selectbox("Choisir un agent:", ["Choisir un agent","Traduction", "Sentiment", "Scrum"])
if selection == "Choisir un agent":
    st.title("Echo Bot")

if selection == "Traduction":
    st.title("Echo Bot : Traduction")
    # React to user input
    if prompt := st.chat_input("Ecrivez à l'Agent Traduction"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        #response = get_ner(client, prompt)
        response, last_interactions = get_agent_response(client, prompt)
        traduction_results = eval(response)
        #print(traduction_results)



        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
elif selection == "Sentiment":
    st.title("Echo Bot : Sentiment")
    # React to user input
    if prompt := st.chat_input("Ecrivez à l'Agent Sentiment"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        #response = get_ner(client, prompt)
        response, last_interactions = get_agent_sentiment_response(client, prompt)
        traduction_results = eval(response)
        #print(traduction_results)



        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

elif selection == "Scrum":
    st.title("Echo Bot : Scrum")
    # React to user input
    if prompt := st.chat_input("Ecrivez à l'Agent Scrum"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        #response = get_ner(client, prompt)
        response, last_interactions = get_agent_scrum_response(client, prompt)
        traduction_results = eval(response)
        #print(traduction_results)



        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})





