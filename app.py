import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

def get_chat_model_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input_text = st.text_input("Input: ", key="input")
if st.button("Ask the question"):
    response = get_chat_model_response(input_text)
    st.subheader("The Response is")
    st.write(response)
