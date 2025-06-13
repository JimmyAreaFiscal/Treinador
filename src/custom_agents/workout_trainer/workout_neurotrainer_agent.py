from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv

load_dotenv()

INSTRUCTIONS = (
    "You are a neurological researcher, specialized in superbike racing performance improvement based on neuroscience."
    "You are given the current neurological condition of the athlete and the microcycle goal. "
    "You should first think on the best neurological improvements to achieve during the microcycle and neurolocial condition"
    "Then, you should generate a neurological training plan for the athlete, based on the microcycle goal and the current neurological condition of the athlete."

    "The neurological training plan should be in the form of a list of neurological exercises, with the description of the exercises, the number of tried and the reason for the exercise."
    "Use only neurological exercises that are able to be performed using smartphone apps or notebooks. Also, return the answer in brazilian portuguese."
    
)


class NeurologicalExercise(BaseModel):
    name: str = Field(description="The name of the exercise")
    description: str = Field(description="The description of the exercise")
    frequency: str = Field(description="The frequency of the exercise")
    reason: str = Field(description="The reason for performing the exercise")


class NeurologicalDailyRoutine(BaseModel):
    weekday: str = Field(description="The day of the week to perform the workout")
    exercises: list[NeurologicalExercise] = Field(description="The list of exercises to perform")

class NeurologicalTrainingPlan(BaseModel):
    daily_routines: list[NeurologicalDailyRoutine] = Field(description="The list of daily routines to perform")


neurotrainer_agent = Agent(
    name="NeurotrainerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=NeurologicalTrainingPlan,
)