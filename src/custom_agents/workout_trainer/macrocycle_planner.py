from pydantic import BaseModel, Field
from custom_agents.workout_trainer.microcycle_planner import Microcycle
from custom_agents.workout_trainer.test_planner_agent import TestPlan, test_planner_agent
from agents import Agent

INSTRUCTIONS = (
    "You are a workout training planner for superbike racing athletes. "

    "Your objective is to improve the perfomance of the athlete in the next 3 months by upgrading his physical condition, neurological condition and flexibility."

    "You are given the user input and the sport specific details. "

    "You should run the following steps in order: "
    "1. Think on the areas where the athlete should improve his condition to achieve a performance improvement. "

    "2. Generate the microcycle objectives based on the macrocycle objective and the athlete's datas. Each microcycle has a duration of 4 weeks, and should be focused on improving a specific aspect of the athlete's condition. The microcycle objectives examples are: improve strength, improve muscular resistance, improve cardiovascular endurance, improve equilibrium and flexibility. Do not be as specific as 'improve strength of the left leg', but rather 'improve strength' or 'improve muscular resistance' or 'improve cardiovascular endurance' or 'improve equilibrium and flexibility'."

    "3. Explain how the microcycles objectives will improve the athlete's condition, and how it will lead to the macrocycle objective."
    
    "4. Generate the test plan by calling the TestPlannerAgent tool only once, using sport details as input. Do not call the tool again after it has been used."

    "5. After generated the test plan, return the answer in brazilian portuguese."

    "You can use the following tools to help you: "
    "1. Test assistant: to select the best tests to perform to measure the improvement of the athlete's condition. "

    "After using the tool, include its result in your final output and return the complete response in brazilian portuguese without calling the tool again."
    
)

test_planner_tool = test_planner_agent.as_tool(
    tool_name="TestPlannerAgent",
    tool_description="A tool to generate the test plan for the macrocycle. You should use this tool to generate the test plan, and you should give him the macrocycle objective and the sport specific details as input."
)

tools = [test_planner_tool]

class Macrocycle(BaseModel):
    description: str = Field(description="A description of the macrocycle, explaining what to focus on, what to improve and what it will lead to")
    microcycles: list[Microcycle] = Field(description="The list of microcycles to perform")
    tests: TestPlan = Field(description="The test plan to be executed at the beginning and at the end of the macrocycle")


class Objectives(BaseModel):
    description: str = Field(description="A description of the macrocycle, explaining what to focus on, what to improve and what it will lead to")
    microcycles: list[str] = Field(description="The list of microcycles objectives to perform")
    tests: TestPlan = Field(description="The test plan to be executed at the beginning and at the end of the macrocycle")
   

macrocycle_agent = Agent(
    name="MacrocyclePlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=tools,
    handoffs=[],
    output_type=Objectives
    )