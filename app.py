from openai import OpenAI
import streamlit as st

f = open("keys/.key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("AI Code Reviewer")


prompt = st.text_area("Enter the python code", height = 150)

if st.button("Generate") == True:
    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "system", "content": """You are a Python code reviewer. 
                                                 When I provide you a Python code snippet, you have to list the bugs in an unordered list with a heading "Bugs" and provide the corrected code snippet below the bugs list."""},
                {"role": "user", "content": prompt}
                ]
    )
    output = response.choices[0].message.content
    st.write(output)