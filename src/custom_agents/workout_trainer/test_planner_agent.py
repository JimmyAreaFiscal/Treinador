from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a test planner for superbike racing athlete preparation." 
    "Your objective is to measure the improvement of the athlete's performance in physical, neurological and flexibility conditions."
    "You are given a macrocycle objective"
    "You should generate a set of tests exercises to perform to measure the improvement of the athlete's condition in the beginning and in the end of the macrocycle. With that test, the athlete should be able to check if the macrocycle objective has been achieved."
    

    "You can use the following modalities for the tests:"
    "- Running"
    "- Cycling"
    "- Weightlifting in brazilian gyms"
    "- Custom apps made for notebook computers for neurological tests"
    "- Flexibility tests"

    

    "Think before answering, and make sure to follow the instructions carefully."
    "For each test exercise, you should generate its description, the reason for the choice and the expected result at the end of the macrocycle. Be as much as specific as possible, adding many test exercises as needed for each modality. "

    "Test all muscular groups and modalities, focusing on those that are more important for the macrocycle objective improve measurement."

    "Make sure to generate a valid test plan, with the test exercises being explained and justified. Also, make sure to focus on the superbike racing performance, not on general endurance. Also, return the answer in brazilian portuguese."
    
)


class TestExercise(BaseModel):
    modality: str = Field(description="The modality of the test. It should be one of the following: strength, resistance, cardiovascular endurance, flexibility, neurological")
    description: str = Field(description="A description of the test exercise")
    reason: str = Field(description="The reason for the choice of the test exercise")
    expected_result: str = Field(description="The expected result at the end of the macrocycle")


class TestPlan(BaseModel):
    tests: list[TestExercise] = Field(description="The list of test exercises to perform")



test_planner_agent = Agent(
    name="TestPlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=TestPlan,
)