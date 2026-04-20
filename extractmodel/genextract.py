import os 
from dotenv import load_dotenv
 
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603"
)


prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an intelligent information extraction assistant.

Your task is to read the given paragraph and extract all useful information in a clean human-readable format.

Focus on identifying:

1. Title / Name  
2. Type (Movie / Book / Person / Product / Event etc.)  
3. Genre / Category  
4. Release Year / Date  
5. Language  
6. Country / Origin  
7. Director / Creator  
8. Producer / Author / Owner  
9. Main Cast / Important People  
10. Characters and Roles  
11. Story / Main Description  
12. Key Themes / Messages  
13. Famous Quotes / Dialogues  
14. Important Keywords  
15. Any Extra Useful Facts  
16. Quick Summary (1 sentence)

Rules:
- Extract only what is clearly mentioned.
- If something is missing, write "Not Mentioned".
- Keep output clean and structured.
- Make summary short and useful.
- Do not return JSON.
- Be concise but complete.
     """), 

    ("human", """"extract information from the following paragraph: {paragraph}""")
])


para=input("Enter a paragraph to extract information from: ")
final_prompt=prompt.invoke(
  {"paragraph": para}
)


response = model.invoke(final_prompt)
print(response.content)
 