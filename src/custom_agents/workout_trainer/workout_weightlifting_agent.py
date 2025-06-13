from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv

load_dotenv()

INSTRUCTIONS = (
    "You are a weight lifting workout trainer, specialized in superbike racing."
    "You are given a specific main muscle group to target, the current physical condition of the athlete and the microcycle goal. "
    "You should generate a workout routine for that main muscle group, for a day, based on the microcycle goal and the current physical condition of the athlete."

    "The workout routine should be in the form of a list of exercises, with the number of sets, reps, and the percentage of the one rep max to use for the exercise."
    "Use only exercises that are commonly used in brazilian gyms. Also, return the answer in brazilian portuguese."
    
)


class Exercise(BaseModel):
    name: str = Field(description="The name of the exercise")
    sets: int = Field(description="The number of sets to perform")
    reps: int = Field(description="The number of reps to perform")
    rm_percent: int = Field(description="The percentage of the one rep max to use for the exercise")
    reason: str = Field(description="The reason for performing the exercise")


class WorkoutDay(BaseModel):
    weekday: str = Field(description="The day of the week to perform the workout")
    exercises: list[Exercise] = Field(description="The list of exercises to perform")
    main_muscle_group: str = Field(description="The main muscle group to target")



weightlifting_workout_agent = Agent(
    name="WeightliftingWorkoutPlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WorkoutDay,
)