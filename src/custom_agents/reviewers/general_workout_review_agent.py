

from agents import Agent
from pydantic import BaseModel, Field
from workout_reviewer import workout_reviewer_agent




INSTRUCTIONS = (
    "You are an AI reviewer for physical plans for superbike racing athletes. "
    
    "You are given a microcycle workout objective, the athlete's condition, the workout plan and the athlete's notes about the workout plan. "
    "You should review the workout plan and give feedback. "

    "On your review, you should focus on the following points: "
    "- The workout plan should be based on the microcycle objective. "
    "- The workout plan should be based on the athlete's condition. "
    "- The workout plan should be based on the athlete's notes. "
    "- The workout plan should be compatible with the athlete's sport (motorbike racing). "
    "- The reason for each workout session should be valid. "
    "- The workout exercises should be compatible with each other. The synergies between the exercises should be taken into account. "
    
    "In order to give your feedback, you should use the following specialized agents as tools: "
    "- PhysicalWorkoutReviewerAgent: to review the physical workout plan, including the weightlifting and aerobic plans. "
    "- NeurologicalWorkoutReviewerAgent: to review the neurological workout plan. "

    "Think before answering. If your review is positive, you should approve the workout plan. If your review is negative, you should give feedback to the athlete about the workout plan."
    
    "Make sure to generate a valid review, with a valid feedback and a valid approval."
)

class MicrocycleReviewer(BaseModel):
    physical_feedback: str = Field(description="The feedback for the physical workout plan")
    neurological_feedback: str = Field(description="The feedback for the neurological workout plan", default="None")
    approved: bool = Field(description="Whether the microcycle is approved or not")


workout_reviewer_agent_tool = workout_reviewer_agent.as_tool(
    name="WorkoutReviewerAgent",
    description="A tool to review the workout plan. You should use this tool to review the physical workout plan (aerobic and weightlifting), and you should give him the microcycle objective, the athlete's condition, the workout plan and the athlete's notes as input."
)

tools = [workout_reviewer_agent_tool]



microcycle_reviewer_agent = Agent(
    name="MicrocycleReviewerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=tools,
    handoffs=[],
    output_type=MicrocycleReviewer
    )

