from transformers import BertTokenizerFast

def wordpiece(payload = "hello how are you? dimistification of the triskaidekaphobia"):
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")
    token_ids = tokenizer(payload)
    # print(token_ids['input_ids'])

    token_mapping = {}
    for ids in token_ids['input_ids']:
        # print(token)
        token_text = tokenizer.decode(ids, skip_special_tokens=True)
        token_mapping[token_text] = ids
    return {
        "text" : payload,
        "tokens" : token_ids['input_ids'],
        "token_length" : len(token_ids['input_ids']),
        "token_mapping" : token_mapping
    }

