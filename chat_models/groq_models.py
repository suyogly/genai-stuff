from langchain_groq import ChatGroq

def gpt_oss_120b(llm=ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)):
    return llm