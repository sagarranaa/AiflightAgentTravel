from app.state.travel_state import TravelState


def hotel_agent(state: TravelState) -> TravelState:
    """
    Find hotel details and update the travel state.
    """

    print("\n🏨 Hotel Agent Started...")

    # In real application, this could call:
    # - Hotel API
    # - Database
    # - LLM with tools

    hotel_data = {
        "name": "Sea View Resort",
        "location": state.destination,
        "nights": state.days,
        "price": 7000
    }

    # Update shared state
    state.hotel = hotel_data

    print("Hotel selected:")
    print(state.hotel)

    return state