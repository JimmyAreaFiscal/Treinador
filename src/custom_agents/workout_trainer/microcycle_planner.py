from pydantic import BaseModel, Field
from agents import Agent
from custom_agents.workout_trainer.workout_aerobic_agents import AerobicWorkoutPlan, aerobic_workout_agent
from custom_agents.workout_trainer.workout_weightlifting_agent import WorkoutDay, weightlifting_workout_agent
from custom_agents.reviewers.workout_reviewer import WorkoutReviewer, workout_reviewer_agent
import json

INSTRUCTIONS = (
    "You are a workout training planner for superbike racing athletes. "

    "You are given a specific goal for a microcycle from the athlete, his current physical condition and his training availability."

    "You should first come up with an microcycle plan (4 weeks of same weekly training plan) that is specific to the motorbike racing sport and the microcycle goal. Then, you should review the microcycle plan with the WorkoutReviewerAgent tool and modify if it needed based on the feedback"
    
    "Finally, you should return the final and approved microcycle plan as your final output. "

    "The microcycle plan should be in the form of a list of days workouts, with all exercises that should be performed for that day."
    "You can use the following tools to help you: "

    "1. WeightliftingWorkoutPlannerAgent: to select weightlifting exercises for each day and a specific main muscle group. "
    "2. AerobicWorkoutPlannerAgent: to select running exercises for the week and a specific goal (endurance, speed, etc.) "
    "3. WorkoutReviewerAgent: to review the microcycle plan and give feedback to the athlete about the workout plan."


    "Think before answering, and give the reason you've chosen a specific muscle group to target for a day and a specific goal (endurance, speed, etc.) "
    "Make sure to generate a valid microcycle plan, with muscle groups to target not being the same for consecutive days. Keep in mind that the athlete should have at least 1 day of rest per week, and that the microcycle should be 1 month long. Also, make sure to focus on the superbike racing performance, not on general endurance."
    "Also, think about the neurological and flexibility exercises as an additional to the weightlifting and aerobic exercises, not as a replacement. They should be performed in at max 15 minutes per day."

    "At the answer, make sure to include the description of the microcycle, explaining what to focus on, what to improve and what it will lead to. Also, return the answer in brazilian portuguese."
    
)



class WeightliftingWorkoutPlan(BaseModel):
    weight_routine: list[WorkoutDay] = Field(description="The weightlifting routine to perform for the microcycle, for each day of the week")


class Microcycle(BaseModel):
    objective: str = Field(description="The objective of the microcycle")
    duration: int = Field(description="The duration of the microcycle in number of weeks")
    aerobic_plan: AerobicWorkoutPlan = Field(description="The aerobic plan to perform for the microcycle")
    weightlifting_plan: WeightliftingWorkoutPlan = Field(description="The weightlifting plan to perform for the microcycle")
    # flexibility_plan: FlexibilityTrainingPlan = Field(description="The flexibility plan to perform for the microcycle")
    # neurotrainer_plan: NeurologicalTrainingPlan = Field(description="The neurological plan to perform for the microcycle")
    description: str = Field(description="A description of the microcycle, explaining what to focus on, what to improve and what it will lead to")
    last_review: WorkoutReviewer = Field(description="The last review of the microcycle plan, with the feedback and the approval of the athlete")


weightlifting_agent_tool = weightlifting_workout_agent.as_tool(
    tool_name="WeightliftingWorkoutPlannerAgent",
    tool_description="A tool to plan the weightlifting routine for the microcycle"
)

aerobic_agent_tool = aerobic_workout_agent.as_tool(
    tool_name="AerobicWorkoutPlannerAgent",
    tool_description="A tool to plan the aerobic routine for the microcycle"
)

workout_reviewer_agent_tool = workout_reviewer_agent.as_tool(
    tool_name="WorkoutReviewerAgent",
    tool_description="A tool to review the workout plan and give feedback to the athlete about the workout plan. You should use this tool to review the microcycle plan before returning it, and you should give him the microcycle objective, the workout plan and the athlete's notes as input."
)

microcycle_planner_agent = Agent(
    name="MicrocyclePlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[weightlifting_agent_tool, aerobic_agent_tool, workout_reviewer_agent_tool],
    handoffs=[],

    output_type=Microcycle
    )

