from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


llm =HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta", 
                        task="text-generation")


model = ChatHuggingFace(llm=llm)

result=model.invoke("Write a 10 line poem on my daughter gurnaaz and batman being good friends, make it a little darker and grittier")

print(result.content)
