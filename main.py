from app.state.travel_state import TravelState
from app.graph.travel_graph import travel_graph


def main():
    # Initial state
    state = TravelState(
        destination="Goa",
        days=2,
        budget=10000
    )

    print("\n=== INITIAL STATE ===")
    print(state)

    # Let LangGraph execute the workflow
    final_state = travel_graph.invoke(state)

    print("\n=== FINAL STATE AFTER LANGGRAPH ===")
    print(final_state)


if __name__ == "__main__":
    main()