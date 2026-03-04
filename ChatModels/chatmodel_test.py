from pydantic import BaseModel, Field
from typing import Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()


class Person(BaseModel):
    prompt: str = Field(description="Prompt used for extraction")
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    job: str = Field(description="Occupation")
    company: str = Field(description="Company where the person works")

parser = PydanticOutputParser(pydantic_object=Person)


prompt = PromptTemplate(template="""
        Extract structured information from the text. {format_instructions} Text: {text}        """,
            input_variables=["text"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=1.0
)

chain = prompt | llm | parser


text = "Alice is a 30 year old data scientist working at Google."

result = chain.invoke({
    "text": text
})

print(result)