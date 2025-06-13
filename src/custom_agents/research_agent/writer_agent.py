from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a senior researcher tasked with writing a cohesive report for a specific sports performance. "
    "You will be provided with the specific sport name, and some initial research done by a research assistant.\n"
    "You should generate a report based on the research and the sport details, in order to be used by another agent to improve workout and diet plans"
    "The report should be concise and to the point, with only the most relevant information about physical and neurological training for sport performance which are very specific to the sport and not to general workout and diet plans."
    "Keep at max 300 words."
)


class ReportData(BaseModel):
    markdown_report: str = Field(description="The final report")


writer_agent = Agent(
    name="Sports Performance Report Writer",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)