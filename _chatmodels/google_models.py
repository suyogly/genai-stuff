from langchain_google_genai import ChatGoogleGenerativeAI

def gemini_flash_2_5(llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)):
    return llm

