import json
from custom_agents.workout_trainer.microcycle_planner import Microcycle
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB_NAME", "treinador")
COLLECTION_NAME = "training_routines"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]



def save_training_routine(routine: dict) -> str:
    """
    Saves a training routine (as a dict/JSON) to the MongoDB collection.
    Returns the inserted document's ID as a string.
    """
    result = collection.insert_one(routine)
    return str(result.inserted_id) 




def save_microcycle_to_db(microcycle: Microcycle) -> str:
    """
    Saves a Microcycle plan to MongoDB as JSON.
    Returns the inserted document's ID as a string.
    """
    # Convert the Pydajson model to a dict
    microcycle_dict = json.loads(microcycle.model_dump_json())
    return save_training_routine(microcycle_dict)