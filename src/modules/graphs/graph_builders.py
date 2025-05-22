"""


This module is responsible for building the graphs.


"""

from langgraph.graph import StateGraph, END, START 
from modules.reviewers.routers import general_reviewer_router
from modules.reviewers.reviewer_nodes import general_reviewer_node
from modules.sport_expert.sport_expert_node import sport_expert
from modules.utils.schemas import AgentState


from modules.graphs.subgraph_builders import training_subgraph_builder, diet_subgraph_builder
def training_workflow_builder() -> StateGraph:
    """
    This workflow is responsible for the main workflow of the system, responsible for the training and diet plans generation.
    """
    # Conversation workflow
    training_workflow = StateGraph(AgentState)

    training_subgraph = training_subgraph_builder().compile()
    diet_subgraph = diet_subgraph_builder().compile()

    training_workflow.add_node("sport_expert_node", sport_expert)
    training_workflow.add_edge(START, "sport_expert_node")

    training_workflow.add_node("training_subgraph", training_subgraph)
    training_workflow.add_node("diet_subgraph", diet_subgraph)
    training_workflow.add_node("general_review_node", general_reviewer_node)

    training_workflow.add_edge("sport_expert_node", "training_subgraph")
    training_workflow.add_edge("training_subgraph", "diet_subgraph")

    training_workflow.add_edge("diet_subgraph", "general_review_node")

    
    training_workflow.add_conditional_edges(
        "general_review_node",
        general_reviewer_router,
        {
            "approved": END,
            "rejected": "diet_subgraph"
        }
    )
    

    

    
    
    return training_workflow


