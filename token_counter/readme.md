Questions:
1. why does wordpiece tokenizer gives [101] and [102] as special tokens?
2. why doesnt tiktoken give space in the beginning of the tokenized output but wordpiece does?
3. which one generates fewer tokens?
4. do we need to implement tokenizers like tiktoken in RAG?
  

Answers:
1. The WordPiece tokenizer uses [101] and [102] as special tokens to denote the beginning and end of a sequence, respectively. These tokens help the model understand where the input text starts and ends, which is crucial for tasks like classification or sequence generation.
2. TikToken PRESERVES spaces as part of tokens (" world"), WordPiece REMOVES spaces and uses ## for continuation tokens ("##world").
3.
4. We may or maynot use tiktoken in RAG process, however since models have context limits, we can use tiktoken to validate the context limitation from tokens returned by the splitters (RecursiveCharacterTextSplitters -> Langchain) and also when we get context to feed to models (system prompt + tokens returned by splitters + human query).


Journey:



What I realised:
Tokenizer (Preprocessing): Converts "Hello" -> [15496].
Attention Mechanism (Processing): Takes the embedding of [15496], compares it to other tokens, and determines its contextual importance. 