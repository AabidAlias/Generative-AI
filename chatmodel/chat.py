from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-small-2603"
)

def ask_ai(user_text):
    response = model.invoke(user_text)
    return response.content


# Optional standalone test
if __name__ == "__main__":
    reply = ask_ai("write a small mail to my college registrar about my leave of absence for 2 weeks")
    print(reply)