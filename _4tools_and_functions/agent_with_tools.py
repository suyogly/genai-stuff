from langchain.agents import create_agent
from langchain.tools import tool
from _4tools_and_functions.arxiv_paper_retriever import arxiv_retriever
from _chatmodels.groq_models import gpt_oss_120b
from dotenv import load_dotenv
import asyncio
import json
import os

if os.path.exists(".env"):
    load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("GROQ_API_KEY is not set")

@tool("arxiv_retriever")
async def paper_retrieve(query: str):
    """
    this tool searches for the research papers from arxiv
    """
    res = await arxiv_retriever(query=query)
    return res


agent = create_agent(
    model=gpt_oss_120b(),
    tools=[paper_retrieve],
    system_prompt="you are a helpful assistant with tools/functions."
)

async def tooling(query: str):
    result = agent.astream(
        {"messages": [
            {"role": "user", "content": query}
            ]},
        {"configurable": {"thread_id": 1}},
        stream_mode="messages"
        )
    
    async for chunks, metadata in result:
        if chunks.content:
            # await asyncio.sleep(0)
            yield f"data: {json.dumps(chunks.content)}\n\n"