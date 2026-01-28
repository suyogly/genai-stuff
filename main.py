from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from _1token_counter.tokenize_tiktoken import get_tokens
from _1token_counter.tokenize_wordpiece import wordpiece
from _2embeddings._contextual_embeddings import cosine_similarity
from _3chat.stream_chat import Stream_chat

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Your Next.js URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.post("/tiktoken")
def tiktoken_tokens(payload : dict = Body(...)):
   text = payload.get("input", "")
   return get_tokens(payload=text)

@app.post("/wordpiece")
def wordpiece_tokens(payload: dict = Body(...)):
    text = payload.get("input", "")
    return wordpiece(payload=text)
    
@app.post("/compare-tiktoken-wordpiece")
def compare_tiktoken_wordpiece(payload: dict = Body(...)):
   return tiktoken_tokens(payload=payload), wordpiece_tokens(payload=payload)

@app.post("/embeddings")
def contextual_embeddings(payload: dict = Body(...)):
   text = payload.get("input", None)
   data = cosine_similarity(intents=text)
   return data

@app.post("/chat_stream")
def chat_stream(payload: dict = Body(...)):
   user_msg = payload.get("query", "")
   res = Stream_chat(intent=user_msg)
   return StreamingResponse(res, media_type="text/event-stream")
