from arxiv import Client, Search, SortCriterion
import asyncio

client = Client(delay_seconds=1)

async def arxiv_retriever(query: str):
    search = Search(
        query=query,
        max_results=5,
        sort_by=SortCriterion.Relevance
    )

    
    def get_pdf():
        res = client.results(search=search)
        
        papers = []
        for r in res:
            papers.append({"paper": r.title,
                    "author": [author for author in r.authors],
                    "url": r.pdf_url})
        return papers
    
    papers = await asyncio.to_thread(get_pdf)
    return {"papers": papers}
            