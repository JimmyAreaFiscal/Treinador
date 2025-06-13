import os
from agents import Agent, ModelSettings
import aiohttp
from pydantic import BaseModel, Field 
from langchain.tools import StructuredTool 
import arxiv
from openai import AssistantEventHandler


class ArxivArgs(BaseModel):
    query: str = Field(description='Query to search the Arxiv.org')

def search_arxiv(query: str, max_results: int = 5):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    results = []
    for result in client.results(search):
        results.append({
            "title": result.title,
            "summary": result.summary,
            "authors": [a.name for a in result.authors],
            "published": result.published,
            "pdf_url": result.pdf_url,
            "entry_id": result.entry_id,
        })
    return results

tool_arxiv = StructuredTool.from_function(
    func=search_arxiv,
    name="search_arxiv",
    description="Searches arXiv.org for academic papers related to the given query and returns a list of results with title, summary, authors, published date, pdf url, and entry id.",
    args_schema=ArxivArgs,
)


INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web and in the Arxivfor that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)


tools = [tool_arxiv]


search_agent = Agent(
    name="Research Agent",
    instructions=INSTRUCTIONS,
    tools=tools,
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)

