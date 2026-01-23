from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1", temperature=1.2)

result=model.invoke("what makes batman great")

print(result.content) 