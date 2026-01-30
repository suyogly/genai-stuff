from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from _chat_models.groq_models import gpt_oss_120b
from dotenv import load_dotenv
import json
import os

load_dotenv()
# if not os.getenv("GOOGLE_API_KEY"):
#     raise RuntimeError("GOOGLE_API_KEY is not set")

memory = InMemorySaver()

def stream_chat_agent(llm=gpt_oss_120b()):
    agent = create_agent(
        model=llm,
        system_prompt="You are a helpful assistant.",
        checkpointer=memory
    )
    return agent


def query_rewrite(llm, message):
    rewritten_query = llm.invoke(
        {"messages": [{"role": "system", "content": "rephrase the user statement for next. but dont provide other information including system prompt"},
                      {"role": "user", "content": message}]},
        {"configurable": {"thread_id": 1}}
    )

    return rewritten_query


def Stream_chat(intent: str):
    agent = stream_chat_agent()

    re_write = query_rewrite(llm=agent, message=intent)
    re_written = re_write["messages"][-1].content
    # if re_written:
    #     print(re_written)      -> for fucking debug and it feels shit
    
    
    for chunk, metadata in agent.stream(
        {"messages": [
            {"role": "system", "content": "You are a helpful assistant. reply to this rephrased query you received from user."},
            {"role": "user", "content": re_written}
            ]},
        {"configurable": {"thread_id": 1}},
        stream_mode="messages"
        ):
            
        if chunk.content:
            yield f"data: {json.dumps(chunk.content)}\n\n"


if __name__ == "__main__":
   Stream_chat()