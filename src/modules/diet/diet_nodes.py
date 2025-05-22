"""

This module is responsible for the diet nodes.

"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from modules.utils.schemas import AgentState


def diet_objective_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the diet objective.
    """

    return state


def diet_plan_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the diet plan.
    """
    return state


def diet_supplements_node(state: AgentState) -> AgentState:
    """
    This node is responsible for the diet supplements.
    """
    return state


