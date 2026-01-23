### Overview of Embeddings



Questions:
1. what exactly is an embedding? and where does it fit in the whole LLM pipeline, i mean what comes before and after embedding process?
2. why didnt we just feed the tokenized output to the model instead of converting them to embeddings?
3. what exactly is a dense vector and sparse vector?
4. how are embeddings generated?
5. primitive form of embeddings - one hot encoding?
6. what word2vec is and what it solved over one hot encoding? and how does word2vec generate embeddings?
7. what word2vec solved? and why is king - man + woman = queen? and why did we need contextual embeddings later on over word2vec?
8. is contextual embedding a by product of transformer architecture? or is it something different? do i need to understand attention mechanism to understand contextual embeddings?
9. why 300 dimensions? why not 100 or 500? and why that many demensions for a single token?
10. the thing i didnt understand, dont give in md, just plain text:
tokenizer gives ids -> numbers
embedding is made from those numbers
and transformer makes again the contexual embeddings
but the embedding that is fed to the transformer, where does it come from? what procudes it?


Answers:






What I realised:
- Attention does not work directly on embeddings either.
- Attention layers consume embeddings (plus positional info), not token IDs. Contextual embeddings are what come out.
- 