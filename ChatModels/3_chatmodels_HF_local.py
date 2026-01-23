from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

from dotenv import load_dotenv


load_dotenv()


llm =HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                    task="text-generation",
                                    pipeline_kwargs=dict(max_new_tokens=256, temperature=0.7))


model = ChatHuggingFace(llm=llm)


result=model.invoke("my name is daman, write something good about me")

print(result.content)