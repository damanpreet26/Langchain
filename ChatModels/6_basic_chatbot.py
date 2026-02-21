from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

context_list = []

context_list.append(SystemMessage(content="You are a Helpful chatbot"))
while True:
    user_input = input("You: ")
    if user_input == 'exit':
        break
    context_list.append(HumanMessage(content=user_input) )
    result = model.invoke(context_list)
    context_list.append(AIMessage(content=result.content))
    print("AI: ", result.content)
    
print(context_list)    