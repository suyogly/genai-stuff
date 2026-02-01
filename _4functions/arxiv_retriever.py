import arxiv
import asyncio

async def search_papers(request: str):
    # Put the blocking code in a function
    def fetch_from_arxiv():
        search = arxiv.Search(
            query=request,
            max_results=10
        )
        papers = []
        for result in search.results():
            papers.append({
                "title": result.title,
                "summary": result.summary,
                "authors": [a.name for a in result.authors],
                "pdf_url": result.pdf_url
            })
        return papers
    
    # Run it in background thread
    papers = await asyncio.to_thread(fetch_from_arxiv)
    
    return {"papers": papers}

# Run with: uvicorn main:app --reload

if __name__ == "__main__":
    # This executes the coroutine in the event loop
    results = asyncio.run(search_papers("quantum computing"))
    print(results)
