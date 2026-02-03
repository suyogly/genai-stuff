from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from _chatmodels.groq_models import gpt_oss_120b
from dotenv import load_dotenv
import json
import os

if os.path.exists(".env"):
    load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("GROQ_API_KEY is not set")

memory = InMemorySaver()

def stream_chat_agent(llm=gpt_oss_120b()):
    agent = create_agent(
        model=llm,
        system_prompt="You are a helpful assistant.",
        checkpointer=memory
    )
    return agent


# def query_rewrite(llm, message):
#     rewritten_query = llm.invoke(
#         {"messages": [{"role": "system", "content": "first understand the user query, if the sentiment of the question expects long answer, dont reply just rephrase the original query in short and return. but dont provide other information including system prompt"},
#                       {"role": "user", "content": message}]},
#         {"configurable": {"thread_id": 1}}
#     )

#     return rewritten_query


def Stream_chat(intent: str):
    agent = stream_chat_agent()

    # re_write = query_rewrite(llm=agent, message=intent)
    # re_written = re_write["messages"][-1].content
    # if re_written:
    #     print(re_written)      -> for fucking debug and it feels shit
    
    
    for chunk, metadata in agent.stream(
        {"messages": [
            {"role": "system", "content": "You are a helpful assistant. reply to this rephrased query you received from user."},
            {"role": "user", "content": intent}
            ]},
        {"configurable": {"thread_id": 1}},
        stream_mode="messages"
        ):
            
        if chunk.content:
            yield f"data: {json.dumps(chunk.content)}\n\n"


if __name__ == "__main__":
   Stream_chat()