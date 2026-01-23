from fastapi import FastAPI, Body
from _1token_counter.tokenize_tiktoken import get_tokens
from _1token_counter.tokenize_wordpiece import wordpiece

app = FastAPI()

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

  
