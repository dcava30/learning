import streamlit as st
import time
import random


# Define Streamlit app behavior
def response_generator():
    response = random.choice(
        [
            "WAA WAA WEE WAA", 
            "Heck Yeah", 
            "Do you like fishing?", 
            "King of the castle, King of the castle", 
            "I get a window from a glass, he must get a window from a glass. I get a step, he must get a step. I get a clock radio, he cannot afford. Great success!",
            "This is my country of Kazakhstan. It locate between Tajikistan, and Kyrgyzstan, and ****** Uzbekistan.",
            "High five!", 
            "Just a couple of pimps",
            "What's up with it, Vanilla face? Me and my homie Azamat just parked our slab outside.", 
            "Sometime my sister, she show her vazhïn to my brother Bilo and say 'You will never get this you will never get it la la la la la la.' He behind his cage. He cries, he cries and everybody laughs. She goes 'You never get this.' But one time he break cage and he 'get this' and then we all laugh. High five!",
            "I could not concentrate on what this old man was saying.",
            "This is Natalya.",
            "I will look on your treasures, gypsy. Is this understood?"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# API access credentials



# Chatbot Headings 
st.title("Borat Chatbot")
st.text("This chatbot is Agile 1: Skateboard")


# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input / Function for responses
if prompt := st.chat_input("Talk to Borat"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in a chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    

# Display assistant repsonse in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to the chat history
st.session_state.messages.append({"role": "assistant", "content": response})
