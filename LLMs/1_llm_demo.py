from langchain_openai import OpenAI
from dotenv import load_dotenv
from warnings import filterwarnings
filterwarnings("ignore")  # Suppress warnings for cleaner output


load_dotenv()  # Load environment variables from .env file


llm = OpenAI(model="gpt-3.5-turbo-instruct")

result=llm.invoke("how are the people of Punjab?")

print(result)