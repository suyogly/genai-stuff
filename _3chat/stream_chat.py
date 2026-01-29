from langchain_groq import ChatGroq
from langchain.agents import create_agent
from _chat_models.groq_models import gpt_oss_120b
from dotenv import load_dotenv
import json
import os

load_dotenv()
# if not os.getenv("GOOGLE_API_KEY"):
#     raise RuntimeError("GOOGLE_API_KEY is not set")

def stream_chat_agent(llm=gpt_oss_120b()):
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