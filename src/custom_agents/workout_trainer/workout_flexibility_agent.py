from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv

load_dotenv()

INSTRUCTIONS = (
    "You are a yoga, mobility and stretching coach, specialized in superbike racing performance improvement."
    "You are given the current flexibility condition of the athlete and the microcycle goal. "
    "You should first think on the best flexibility improvements to achieve during the microcycle and flexibility condition"
    "Then, you should generate a flexibility training plan for the athlete, based on the microcycle goal and the current flexibility condition of the athlete."

    "The flexibility training plan should be in the form of a list of flexibility exercises, with the description of the exercises, the number of tried and the reason for the exercise."
    "Use only flexibility exercises that are able to be performed using smartphone apps or notebooks. Also, return the answer in brazilian portuguese."
    
)


class FlexibilityExercise(BaseModel):
    name: str = Field(description="The name of the exercise")
    description: str = Field(description="The description of the exercise")
    frequency: str = Field(description="The frequency of the exercise")
    reason: str = Field(description="The reason for performing the exercise")


class FlexibilityDailyRoutine(BaseModel):
    weekday: str = Field(description="The day of the week to perform the workout")
    exercises: list[FlexibilityExercise] = Field(description="The list of exercises to perform")


class FlexibilityTrainingPlan(BaseModel):
    daily_routines: list[FlexibilityDailyRoutine] = Field(description="The list of daily routines to perform")


flexibility_agent = Agent(
    name="FlexibilityAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=FlexibilityTrainingPlan,
)