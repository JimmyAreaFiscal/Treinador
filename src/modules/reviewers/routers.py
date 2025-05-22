"""

This module is responsible for the reviewers routers.

When diet or training plans are rejected, the reviewer will send the plan back to the diet or training expert to make the necessary changes.

"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from modules.utils.schemas import AgentState


def diet_reviewer_router(state: AgentState) -> AgentState:
    """
    This router is responsible for the diet reviewer.
    """
    if state['diet_review'] == 'rejected':
        return 'diet_plan'
    else:
        return 'general_review'


def training_reviewer_router(state: AgentState) -> AgentState:
    """
    This router is responsible for the training reviewer.
    """
    if state['training_review'] == 'rejected':
        return 'training_plan'
    else:
        return 'general_review'


def general_reviewer_router(state: AgentState) -> AgentState:
    """
    This router is responsible for the general reviewer.
    """
    return 'END'