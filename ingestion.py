from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings


load_dotenv()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]   

data = [WebBaseLoader(url).load() for url in urls]

data_list = [item for sublist in data for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)

data_splits = text_splitter.split_documents(data_list)

vectorstore = Chroma.from_documents(
    documents=data_splits,
    collection_name="rag-chroma",
    embedding=OpenAIEmbeddings(model="text-embedding-ada-002"),
    persist_directory="./.chroma",
)

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma",
    embedding_function=OpenAIEmbeddings(model="text-embedding-ada-002"),
).as_retriever()    
