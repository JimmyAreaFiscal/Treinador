"""

This module is responsible for reviewing the training and diet plans.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from modules.utils.schemas import AgentState
from modules.utils.llm import ChatLLM


def training_reviewer_node(state: AgentState) -> AgentState:
    """
    This node is responsible for reviewing the training plan.
    """
    pass


def diet_reviewer_node(state: AgentState) -> AgentState:
    """
    This node is responsible for reviewing the diet plan.
    """
    pass


def general_reviewer_node(state: AgentState) -> AgentState:
    """
    This node is responsible for reviewing the general plan.
    """
    pass


