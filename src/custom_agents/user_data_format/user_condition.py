
from pydantic import BaseModel, Field

class UserHealthCondition(BaseModel):
    """
    This is a pydantic model that contains the current physical condition of the user.
    """
    sport: str = Field(description="The sport the user is training for", default="Superbike Racing")
    weight: float = Field(description="The weight of the user in kilograms")
    height: float = Field(description="The height of the user in centimeters")
    age: int = Field(description="The age of the user", default=30)
    gender: str = Field(description="The gender of the user", default="Male")

    experience: str = Field(description="The experience of the user in the sport", default="Amateur")
    injuries: str = Field(description="The injuries the user has.", default="None")
    aerobic_modalities: list[str] = Field(description="The aerobic modalities the user is interested in", default=["Running", "Cycling"])
    
    notes: str = Field(description="Any other information about the user that is not covered by the other fields", default="None")

    
class UserTrainingAvailability(BaseModel):
    """
    This is a pydantic model that contains the training availability of the user.
    """
    training_availability: str = Field(description="The training availability of the user", default="From monday to friday, two sessions per day, one in the morning and one in the evening, each one lasting 1 hour")

class UserLastTestResults(BaseModel):
    """
    This is a pydantic model that contains the last test results of the user.
    """
    last_test_results: str = Field(description="The last test results of the user", default="None")

class UserLastMacrocycle(BaseModel):
    """
    This is a pydantic model that contains the last macrocycle of the user.
    """
    last_macrocycle: str = Field(description="The last macrocycle objective of the user", default="Resistance improvement")

class UserInput(BaseModel):
    """
    This is a pydantic model that contains all the input of the user.
    """
    user_health_condition: UserHealthCondition = Field(description="The health condition of the user")
    user_training_availability: UserTrainingAvailability = Field(description="The training availability of the user")
    user_last_test_results: UserLastTestResults = Field(description="The last test results of the user")
    user_last_macrocycle: UserLastMacrocycle = Field(description="The last macrocycle objective of the user")