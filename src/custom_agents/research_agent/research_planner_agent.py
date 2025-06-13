from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 12

INSTRUCTIONS = f"""You are a helpful research assistant. 
Given a specific sport, come up with a set of web searches items related to the aspects of the sport, like physical training and neurological training for the best athletes of that sport.

Focus on the following aspects:
- Microcycles of training for the sport
- Macrocycles routines for the sport
- Athlete's physical condition required to well perform in the sport 
- Athlete's neurological condition required to well perform in the sport
- Key physical and neurological factors that influence the sport performance
- Other relevant aspects

Output at least {HOW_MANY_SEARCHES} terms to query for."""


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    

research_planner_agent = Agent(
    name="Research Planner Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)