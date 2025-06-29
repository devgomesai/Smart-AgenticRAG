from dotenv import load_dotenv
from graph.graph import graph
load_dotenv()

if __name__ == '__main__':
    print("Hello Advanced RAG")
    
    user_input = str(input("Enter Query: "))
    
    while user_input not in ['bye', 'quiet', 'q']:
        response = graph.invoke(input={"question": user_input})
        
        print('-'*30)
        print(response['generation'])
        print('-'*30)
        print(response['web_search'])
        print('-'*30)
        print(response['docs'])
        print('-'*30)
    print('GoodBye!......')