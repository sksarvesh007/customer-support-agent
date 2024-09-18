from langchain_groq import ChatGroq
import os 
import dotenv 
from scraper import web_content
dotenv.load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field


groq_api_key = os.getenv("groq_api_key")
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=2048,
    timeout=None,
    max_retries=2,
    groq_api_key = groq_api_key
)

class contentremover(BaseModel):
    template_compatibility : str = Field(
        description = "Only return with the relevant content of the website in context of the provided questions "
    )
structured_llm_grader = llm.with_structured_output(contentremover)
system = """You are a professional content writer , you are being provided with the markdown content of the particular webpage of the product , you need to 
return with the content that is only relevant to the questions provided in the context . 
"""
content_removing = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "content : {content} , question : {question}"),
    ]
)
final_content = content_removing | structured_llm_grader
