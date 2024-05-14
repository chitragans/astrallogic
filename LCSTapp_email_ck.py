import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email

    Please start the email with a warm introduction. Add the introduction if you need to.
    
    Below is the email:
    EMAIL: {email}
    
    RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["email"],
    template=template,
)

def load_LLM(openai_api_key):
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="Convert Text to Email")
st.markdown("## Enter Your Email To Convert")

def get_api_key():
    #input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    input_text = st.text_input(label="OpenAI API Key ",  type="password", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()

def get_text():
    input_text = st.text_area(label="Type here", placeholder="Your Email...", key="email_input")
    return input_text

email_input = get_text()

if len(email_input.split(" ")) > 700:
    st.write("Please enter a shorter email up to a max of 700 words")
    st.stop()

st.markdown("### Here is your Drafted Email:")

if email_input:
    if not openai_api_key:
        st.warning('Enter your OpenAI API Key.)', icon="🔥")
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    #prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    prompt_with_email = prompt.format(email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)
