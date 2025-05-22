"""

This module is responsible for researching sport expert informations in order to improve the training and diet plans.

"""
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.messages import SystemMessage, HumanMessage
from modules.utils.schemas import AgentState, ExpertInformations
from modules.utils.llm import ChatLLM
from modules.utils.prompts import SPORT_EXPERT_PROMPT_TEMPLATE
import logging

logging.basicConfig(level=logging.INFO)

def sport_expert(state: AgentState) -> AgentState:
    logging.info("Entering sport_expert")

    system_prompt = SPORT_EXPERT_PROMPT_TEMPLATE.format(main_sport=state['main_sport'])

    
    sport_expert_prompt = ChatPromptTemplate.from_template(system_prompt)

    llm = ChatLLM
    structured_llm = llm.with_structured_output(ExpertInformations)
    
    sport_expert_llm = sport_expert_prompt | structured_llm 
    result = sport_expert_llm.invoke({})
    
    state['sport_expert_informations'] = result
    logging.info(f"sport_expert: sport_expert_informations = {state['sport_expert_informations']}")

    return state 