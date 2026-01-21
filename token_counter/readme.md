Questions:
1. why does wordpiece tokenizer gives [101] and [102] as special tokens?
2. why doesnt tiktoken give space in the beginning of the tokenized output but wordpiece does?
3. which one generates fewer tokens?
4. do we need to implement tokenizers like tiktoken in RAG?
5. how does bpe know how to tokenize a word? for example it tokenizes word "this" or any other common english words, but how does it tokenize long words? and how does it understand the small known words? what's the catch?
  

Answers:
1. The WordPiece tokenizer uses [101] and [102] as special tokens to denote the beginning and end of a sequence, respectively. These tokens help the model understand where the input text starts and ends, which is crucial for tasks like classification or sequence generation.
2. TikToken PRESERVES spaces as part of tokens (" world"), WordPiece REMOVES spaces and uses ## for continuation tokens ("##world").
3.
4. We may or maynot use tiktoken in RAG process, however since models have context limits, we can use tiktoken to validate the context limitation from tokens returned by the splitters (RecursiveCharacterTextSplitters -> Langchain) and also when we get context to feed to models (system prompt + tokens returned by splitters + human query).
5. Byte Pair Encoding (BPE) does not know words in a linguistic sense; instead, it uses a purely statistical approach based on frequency to determine how to split text. Because words like "this," "the," or "is" appear extremely frequently in training data, the algorithm repeatedly merges their individual characters until the entire word becomes a single token in the final vocabulary. If a word is long or rare, it likely wasn't frequent enough to be merged into a single token. BPE instead breaks it down into the largest subword units it does recognize, such as un + happi + ness.

However, this is objective, the primary catch is that BPE is entirely data-dependent and lacks actual language understanding so the result varies with the data you provide. Suppose, "this is a good coffee" is the data you ingested, since there are no words that repeated, it actually works on character level. It checks the "pair of words". The tokenizer checks its learned list of merges eg., Rule 1: t + h -> th; Rule 2: th + i -> thi. It continues merging the characters until no more rules from its vocabulary can be applied.


The algorithm counts every adjacent pair across the entire list: 

    For "this is a good coffee",
    The "is" case: The pair i s appears in "this" and "is". It has a frequency of 2.
    The "oo" case: The pair o o appears in "good" and "cooffee". It also has a frequency of 2.
    The "ee" case: The pair e e appears once in "cooffee". It has a frequency of 1.


Because BPE is non-deterministic when frequencies are tied, it will pick one of the pairs with the highest frequency (either i s or o o) based on its internal implementation (often alphabetical or based on which appeared first). If it picks i s, your "is" word becomes one token, and "this" becomes t h is

Journey:



What I realised:

- Clarification on Tokenizers and Attention Mechanism
    - Tokenizer (Preprocessing): Converts "Hello" -> [15496].
    - Attention Mechanism (Processing): Takes the embedding of [15496], compares it to other tokens, and determines its contextual importance. 
