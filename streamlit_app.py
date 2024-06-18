import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

## Define Client for OpenAI
client = OpenAI(
    #api_key=st.text_input(label="API Key ",  type="password", placeholder="Ex: sk-2Cb8un4...", key="api_key_input"),
    api_key="c45e8e03e070469bbea48b070fd8eaf1" ,
    base_url="https://api.aimlapi.com",
)
response = client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
            },
              {
                  "role": "user",
                  "content": "Can you tell me a tamil fish curry recipe?"
              }
             ],
    )
message =response.choices[0].message.content
st.write(message)


#openai_api_key = st.sidebar.text_input('OpenAI API Key')

#def generate_response(input_text):
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
# st.info(llm(input_text))

#with st.form('my_form'):
 # text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  #submitted = st.form_submit_button('Submit')
  #if not openai_api_key.startswith('sk-'):
   # st.warning('Please enter your OpenAI API key!', icon='⚠')
  #if submitted and openai_api_key.startswith('sk-'):
   # generate_response(text)
