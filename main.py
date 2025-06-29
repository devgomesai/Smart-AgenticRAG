from dotenv import load_dotenv
from graph.graph import graph
load_dotenv()

if __name__ == '__main__':
    print("-- Hello Advanced RAG -- ")
    
    while True:
        user_input = str(input("Enter Query: "))
        
        if user_input in ['bye','q']:
            print("GoodBye...")
            break
        
        response = graph.invoke(input={"question": user_input})
        
        print('-' * 30)
        print("🔎 Generation:\n", response.get('generation', 'No generation found'))
        print('-' * 30)
        print("🌐 Web Search:\n", response.get('web_search', 'No web results'))
        print('-' * 30)
        print("📄 Docs:\n", response.get('docs', 'No documents found'))
        print('-' * 30)
        
        