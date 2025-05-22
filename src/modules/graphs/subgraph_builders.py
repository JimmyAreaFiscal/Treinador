"""

This module is responsible for building the subgraphs for the main workflow.

"""



from langgraph.graph import StateGraph, START, END
from modules.reviewers.reviewer_nodes import training_reviewer_node
from modules.diet.diet_nodes import diet_objective_node, diet_plan_node, diet_supplements_node
from modules.reviewers.routers import training_reviewer_router, diet_reviewer_router
from modules.training.training_nodes import training_objective_node, test_development_node, training_plan_node, gym_trainer_node, aerobic_trainer_node, stretching_trainer_node
from modules.reviewers.reviewer_nodes import diet_reviewer_node, training_reviewer_node

from modules.utils.schemas import AgentState
def training_subgraph_builder() -> StateGraph:
    """
    This subgraph is responsible for the training plan generation.
    """
    training_subgraph = StateGraph(AgentState)

    training_subgraph.add_node("training_objective_node", training_objective_node)
    training_subgraph.add_node("test_development_node", test_development_node)
    training_subgraph.add_node("training_plan_node", training_plan_node)
    
    training_subgraph.add_node("gym_trainer_node", gym_trainer_node)
    training_subgraph.add_node("aerobic_trainer_node", aerobic_trainer_node)
    training_subgraph.add_node("stretching_trainer_node", stretching_trainer_node)
    training_subgraph.add_node("training_reviewer_node", training_reviewer_node)
    
    training_subgraph.add_edge(START, "training_objective_node")
    training_subgraph.add_edge("training_objective_node", "test_development_node")
    training_subgraph.add_edge("test_development_node", "training_plan_node")
    
    training_subgraph.add_conditional_edges(
        "training_plan_node",
        training_reviewer_router,
        {
            "gym": "gym_trainer_node",
            "aerobic": "aerobic_trainer_node",
            "stretching": "stretching_trainer_node",
            "review": "training_reviewer_node"
        }
    )

    training_subgraph.add_conditional_edges(
        "training_reviewer_node",
        training_reviewer_router,
        {
            "approved": END,
            "rejected": "training_plan_node"
        }
    )
    return training_subgraph


def diet_subgraph_builder() -> StateGraph:
    """
    This subgraph is responsible for the diet plan generation.
    """
    diet_subgraph = StateGraph(AgentState)

    diet_subgraph.add_node("diet_objective_node", diet_objective_node)
    diet_subgraph.add_node("diet_plan_node", diet_plan_node)
    diet_subgraph.add_node("diet_supplements_node", diet_supplements_node)
    diet_subgraph.add_node("diet_reviewer_node", diet_reviewer_node)

    diet_subgraph.add_edge(START, "diet_objective_node")
    diet_subgraph.add_edge("diet_objective_node", "diet_plan_node")
    diet_subgraph.add_edge("diet_plan_node", "diet_supplements_node")
    diet_subgraph.add_edge("diet_supplements_node", "diet_reviewer_node")

    diet_subgraph.add_conditional_edges(
        "diet_reviewer_node",
        diet_reviewer_router,
        {
            "approved": END,
            "rejected": "diet_plan_node"
        }
    )
    return diet_subgraph

