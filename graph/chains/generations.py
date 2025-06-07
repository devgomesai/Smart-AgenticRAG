from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatOpenAI(model=os.getenv("LLM"), temperature=0)

prompt = hub.pull("rlm/rag-prompt") 

chain = prompt | llm | StrOutputParser()