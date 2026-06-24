from langgraph.graph import StateGraph, START, END

from app.state.travel_state import TravelState

from app.agents.flight_agent import flight_agent
from app.agents.hotel_agent import hotel_agent
from app.agents.budget_agent import budget_agent
from app.agents.optimizer_agent import optimizer_agent


# Create graph with shared state
graph = StateGraph(TravelState)


# ---------------------------
# Add Nodes (Agents)
# ---------------------------

graph.add_node("flight", flight_agent)
graph.add_node("hotel", hotel_agent)
graph.add_node("budget", budget_agent)
graph.add_node("optimizer", optimizer_agent)


# ---------------------------
# Add Normal Edges
# ---------------------------

# START -> Flight
graph.add_edge(START, "flight")

# Flight -> Hotel
graph.add_edge("flight", "hotel")

# Hotel -> Budget
graph.add_edge("hotel", "budget")


# ---------------------------
# Conditional Edge Function
# ---------------------------

def budget_router(state: TravelState):
    """
    Decide where to go after Budget Agent.
    """

    if state.within_budget:
        return END

    return "optimizer"


# ---------------------------
# Add Conditional Edge
# ---------------------------

graph.add_conditional_edges(
    "budget",
    budget_router
)


# ---------------------------
# Loop Edge
# ---------------------------

# Optimizer -> Budget
graph.add_edge(
    "optimizer",
    "budget"
)


# ---------------------------
# Compile Graph
# ---------------------------

travel_graph = graph.compile()