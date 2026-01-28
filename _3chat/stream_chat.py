from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
import json
import os

load_dotenv()
# if not os.getenv("GOOGLE_API_KEY"):
#     raise RuntimeError("GOOGLE_API_KEY is not set")

def stream_chat_agent(llm=ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)):
    agent = create_agent(
        model=llm,
        system_prompt="You are a helpful assistant."
    )
    return agent

def Stream_chat(intent: str):
    agent = stream_chat_agent()
    
    for chunk, metadata in agent.stream(
        {"messages": [{"role": "user", "content": intent}]},
        stream_mode="messages"):
            
        if chunk.content:
            yield f"data: {json.dumps(chunk.content)}\n\n"

if __name__ == "__main__":
   Stream_chat()