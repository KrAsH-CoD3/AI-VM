import config
from openai import OpenAI

api_key = config.DevelopmentConfig.OPENAI_KEY
client = OpenAI(api_key=api_key)

def generateChatResponse(prompt: str):
    messages: list = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    try:
        answer: str = response.choices[0].message.content.replace('\n', '</br>')
    except:
        answer: str = "Oops an Error occured, Try another question, If the problem persits"

    return answer

# while True:
#     prompt = input("You: ")
#     if prompt == "/": break
#     print(f"AI: {generateChatResponse(prompt)}")

