from dotenv import load_dotenv
from graph.graph import graph
load_dotenv()

if __name__ == '__main__':
    print("Hello Advanced RAG")
    user_input = str(input("Enter Query: "))
    print(graph.invoke(input={"question": user_input}))