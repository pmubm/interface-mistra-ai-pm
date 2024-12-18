import streamlit as st
from utiles import get_ner
from mistralai import Mistral


client = Mistral(api_key="ay4EXIYW5M1jqCtssLjyzRnZjkKwbA5f")

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])







# side bar select
selection = st.sidebar.selectbox("Choisir un agent:", ["Traduction", "Entitees"])


if selection == "Traduction":
    pass
elif selection == "Entitees":
    pass






# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = get_ner(client, prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})