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

questions = ""
with open ("question.txt", "r") as f:
    questions = f.read()
questions = questions.split("\n")

class questionanswer(BaseModel):
    template_compatibility : str = Field(
        description = "Return with the answer of the question provided in the context of the content"
    )
structured_llm_grader = llm.with_structured_output(questionanswer)
system = """ You are a professional question answerer , you are being provided with the content of the particular webpage of the product , you need to
give detailed response of how the question is supposed to be answered with respect to the product
"""
question_answering = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "content : {content} , question : {question}"),
    ]
)
question_answerer = question_answering | structured_llm_grader
