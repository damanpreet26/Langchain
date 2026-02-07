from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

from dotenv import load_dotenv


load_dotenv()


llm =HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                    task="text-generation",
                                    pipeline_kwargs=dict(max_new_tokens=256, temperature=0.7))


model = ChatHuggingFace(llm=llm)


result=model.invoke("write a poem on me and y wife, my name is daman and her name is Mandeep, make it romantic and heartfelt")

print(result.content)