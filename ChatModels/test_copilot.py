from langchain_huggingface import HuggingFacePipeline
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from pydantic import BaseModel, Field
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()


# Define your Pydantic model
class PersonInfo(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")
    location: str = Field(description="The person's location")

# Initialize HuggingFace model
# hf_pipeline = pipeline("text-generation", model="gpt2")

# hf_pipeline = pipeline(
#     "text-generation",
#     model="google/gemma-2b-it",
#     max_new_tokens=100
# )

hf_pipeline = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=100
)


llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Create output parser
parser = PydanticOutputParser(pydantic_object=PersonInfo)

# Create prompt template
prompt = PromptTemplate(
    template="Extract person information:\n{format_instructions}\n{query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Create chain
chain = prompt | llm | parser

# Run the chain
result = chain.invoke({"query": "John is 30 years old and lives in New York"})
print(result)