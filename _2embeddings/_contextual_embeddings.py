from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embedder = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    task_type="semantic_similarity"
)

def cosine_similarity(intents: list[str]) -> dict:
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
            "first-word" : {
                intents[0] : "vec1"
            },
            "sec-word" : {
                intents[1] : "vec2"
            },
            "similarity" : cosine_sim
        }

@tool("data_feed")
def data_feed():
    """
    Tool to get similarity data between two words.
    """
    all_data = cosine_similarity()
    first_word = [list(all_data['first-word'].keys())[0]]
    second_word = [list(all_data['sec-word'].keys())[0]]
    similarity = all_data['similarity']
    return {"first_word": first_word, "second_word": second_word, "similarity": similarity}


def explainer_agent(llm = ChatGroq(model = "openai/gpt-oss-120b",temperature = 0.7)):
    agent = create_agent(
        model=llm,
        tools=[data_feed],
        system_prompt="you are a helpful assistant, which gives 2 sentence reasoning of why the two different words have the similarity score of x, and dont reveal internal tool usage. and dont forget to mention the similarity score in percentage with decimal points."
    )

    res = agent.invoke({"messages": [{"role": "user", "content": "call the similarity tool anf follow the system prompt"}]})

    return res["messages"][-1].content


print(explainer_agent())