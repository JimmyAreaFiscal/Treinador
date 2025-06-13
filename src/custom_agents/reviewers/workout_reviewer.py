

from agents import Agent
from pydantic import BaseModel, Field


INSTRUCTIONS = (
    "You are a workout planner reviewer for superbike racing athletes. "
    "You are given a workout plan for a microcycle (4 weeks of the same weekly training plan), the microcycle objective and the athlete's notes about the workout plan. "
    "You should review the phyisical workout routine (aerobic and weightlifting), and check for: "
    "- The workout plan should be based on the microcycle objective. "
    "- The workout plan should consider the athlete's notes. "
    "- The workout plan should be compatible with the athlete's sport (motorbike racing). "
    "- The reason for each workout session should be valid. "
    "- The workout exercises should be compatible with each other. The synergies between the exercises should be taken into account. "


    "Think before answering, and give the reason you've approved or not the workout plan. "
    "Make sure to generate a valid review, with a valid feedback and a valid approval. In your feedback, you should give the reason of your approval or disapproval, and give instructions to the planner agent to improve the workout plan."
)


class WorkoutReviewer(BaseModel):
    feedback: str = Field(description="The feedback for the workout")
    approved: bool = Field(description="Whether the workout is approved or not")


workout_reviewer_agent = Agent(
    name="WorkoutReviewerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[],
    handoffs=[],
    output_type=WorkoutReviewer
    )

