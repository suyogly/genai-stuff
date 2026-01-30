import os
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv # fuck it off in prod
import numpy as np 

if os.path.exists(".env"):
    load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set")

embedder = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    task_type="semantic_similarity"
)

def cosine_similarity(intents):
    """
    Calculates similarity between exactly two strings in a list.
    Example input: ["apple", "banana"]
    """
    try:
        vec1 = embedder.embed_query(intents[0])
        vec2 = embedder.embed_query(intents[1])

    except IndexError as e:
        return {"error" : f"Requires at least 2 words/phrases -> {str(e)}"}
    
    else:
        cosine_sim = round(float(np.dot(vec1, vec2) * 100), 2)

        return {
            "first-word" : {intents[0] : vec1},
            "sec-word" : {intents[1] : vec2},
            "similarity" : cosine_sim
        }



# def explainer_agent(llm = ChatGroq(model = "openai/gpt-oss-120b",temperature = 0.7)):
#     agent = create_agent(
#         model=llm,
#         tools=[cosine_similarity],
#         system_prompt="you are a helpful assistant who calls data_feed tool, which gives 2 sentence reasoning of why the two different words have the similarity score of x, and dont reveal internal tool usage. and dont forget to mention the similarity score in percentage with decimal points."
#     )

#     res = agent.invoke({"messages": [{"role": "user", "content": "call the similarity tool anf follow the system prompt"}]})

#     return {res['messages'][-1].content}


# if __name__ == "__main__":
#     explainer_agent()