import tiktoken

def get_tokens(payload):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(payload)

    token_mapping = {}
    token_texts = []
    for token in tokens:
        token_text = encoding.decode([token])
        token_texts.append(token_text)
        token_mapping[token_text] = token

    return {
        "tiktoken": {
            "text" : payload,
            "tokens" : tokens,
            "token texts" : token_texts,
            "number of tokens" : len(tokens),
            "token map" : token_mapping
    }}