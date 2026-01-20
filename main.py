from fastapi import FastAPI, Body
from token_counter.tokenize_tiktoken import get_tokens

app = FastAPI()

@app.post("/tiktoken")
def tiktoken_tokens(payload : dict = Body(...)):
   text = payload.get("input", "")
   return get_tokens(payload=text)
    

if __name__ == "__main__":
    tiktoken_tokens()
