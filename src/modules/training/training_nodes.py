"""

This module is responsible for the training nodes.

"""

from lib2to3.pytree import Node
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from modules.utils.schemas import AgentState, AthleteConditions, TrainingParams, ExpertInformations, Macrocycle, PhysicalTest
from modules.utils.llm import ChatLLM
from modules.utils.prompts import TRAINING_OBJECTIVE_PROMPT_TEMPLATE, TEST_PROMPT_TEMPLATE

def training_objective_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the training objective.
    """
    
    prompt = ChatPromptTemplate.from_template(TRAINING_OBJECTIVE_PROMPT_TEMPLATE)
    llm = ChatLLM(prompt)
    
    conditions = state["athlete_conditions"]
    params = state["training_params"]
    expert_informations = state["sport_expert_informations"]

    response = llm.invoke(
        {
            "athlete_conditions": conditions,
            "training_params": params,
            "sport_expert_informations": expert_informations
        }
    )

    state["training_objective"] = response

    return state


def test_development_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the test development.
    """
    prompt = ChatPromptTemplate.from_template(TEST_PROMPT_TEMPLATE)
    llm = ChatLLM(prompt)
    llm_with_structured_output = llm.with_structured_output(PhysicalTest)

    response = llm_with_structured_output.invoke(
        {
            "main_sport": state["training_params"].main_sport,
            "objective": state["training_objective"]
        }
    )

    state["physical_test"] = response

    return state

    


def training_plan_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the training plan.
    """
    objective = state["training_objective"]
    main_sport = state["training_params"].main_sport
    test = state["physical_test"]

    

    return state


def gym_trainer_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the gym trainer.
    """
    return state


def aerobic_trainer_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the aerobic trainer.
    """
    return state


def stretching_trainer_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the stretching trainer.
    """
    return state


