from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model="gpt-4", temperature=0.7)


result = model.invoke("write about nikon z5ii")
                      
print(result.content)