from langchain_openai import ChatOpenAI
# from langchain_core import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate 

load_dotenv()


st.header("Tutor App")

# inputs
role = st.selectbox("Select Role",["Doctor", "Engineer", "IT Professional", "Finance Expert", "Dummy"])
words = st.slider("Number of words", min_value=20, max_value=200, value=100, step=10)

#template
template =  PromptTemplate(template="You are an experienced {role}. Please share your expertise and knowledge in this field in around {words} words",
                        input_variables=["role", "words"])

##model
model = ChatOpenAI(model="gpt-4", temperature=1)

##chain
chain = template | model

##invoke
if st.button("Get details"):
    result = chain.invoke({"role": role, "words": words})
    st.write(result.content)
