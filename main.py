from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview", temperature=0.5)
chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    chat_history.append(result.content[0]["text"])
    print("AI: ",result.content[0]["text"])
    
print(chat_history)