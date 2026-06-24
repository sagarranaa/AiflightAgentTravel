from app.state.travel_state import TravelState


def flight_agent(state: TravelState) -> TravelState:
    """
    Find flight details and update the travel state.
    """

    print("\n✈️ Flight Agent Started...")

    # In the real world, this could call:
    # - Flight API
    # - Database
    # - LLM with tools

    flight_data = {
        "airline": "Indigo",
        "departure": "Mumbai",
        "destination": state.destination,
        "price": 4500
    }

    # Update shared state
    state.flight = flight_data

    print("Flight selected:")
    print(state.flight)

    return state