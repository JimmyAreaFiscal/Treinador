from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a aerobic workout trainer, speacialized into superbike racing athlete preparation." 
    "You are given the current physical condition of the athlete and the microcycle goal. "
    "You should generate a workout routine for each da of the week, based on the microcycle goal and the current physical condition of the athlete."

    "You can use the following modalities:"
    "- Running"
    "- Cycling"

    "The workout routine should be in the form of a list of training sessions, with the modality, the duration, the intensity and the reason for performing the session."

    "Think before answering, and make sure to follow the instructions carefully."
    "Make sure to generate a valid workout plan, with valid modalities, durations, intensities and reasons. Also, make sure to focus on the superbike racing performance, not on general endurance. Finally, leave at least 1 day of rest per week. Also, return the answer in brazilian portuguese."
    
)


class Session(BaseModel):
    weekday: str = Field(description="The day of the week to perform the workout")
    modality: str = Field(description="The modality of the session")
    duration: int = Field(description="The duration of the session in minutes")
    intensity: int = Field(description="The intensity of the session")
    description: str = Field(description="A description of the session training, explaining what the athlete should do before, during and after the session")
    reason: str = Field(description="The reason for performing the session")


class AerobicWorkoutPlan(BaseModel):
    sessions: list[Session] = Field(description="The list of sessions to perform")



aerobic_workout_agent = Agent(
    name="AerobicWorkoutPlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=AerobicWorkoutPlan,
)