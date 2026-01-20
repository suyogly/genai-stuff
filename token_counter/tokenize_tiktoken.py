import tiktoken

def get_tokens(payload):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(payload)

    token_mapping = {}
    for token in tokens:
        token_text = encoding.decode([token])
        token_mapping[token_text] = token

    return {"text" : payload,
            "tokens" : tokens,
            "number of tokens" : len(tokens),
            "token map" : token_mapping}