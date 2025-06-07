from typing import Any, Dict
from langchain.schema import Document
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from graph.state import GraphState

load_dotenv()

websearch_tool = TavilySearch(max_results=3)


def web_search(state:GraphState) -> Dict[str,Any]:
    print('-- Web Search --')
    question = state['question']
    docs = state['docs']
    
    tavily_results = websearch_tool.invoke({"query": question})
    joined_tavily_result = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results['results']]
    )
    web_results = Document(page_content=joined_tavily_result)
    
    if docs is not None:
        docs.append(web_results)
    else:
        docs = [web_results]
    # print(joined_tavily_result)
    
    
if __name__ == '__main__':
    web_search(state={"question":"agent memory", "docs": None})