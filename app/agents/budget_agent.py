from app.state.travel_state import TravelState


def budget_agent(state: TravelState) -> TravelState:
    """
    Calculate total trip cost and check whether it fits the budget.
    """

    print("\n💰 Budget Agent Started...")

    # Get flight and hotel prices
    flight_price = state.flight["price"] if state.flight else 0
    hotel_price = state.hotel["price"] if state.hotel else 0
    # Calculate total cost
    total_cost = flight_price + hotel_price
    # Update state
    state.total_cost = total_cost
    # Make decision
    state.within_budget = total_cost <= state.budget
    print(f"Flight Cost: ₹{flight_price}")
    print(f"Hotel Cost: ₹{hotel_price}")
    print(f"Total Cost: ₹{total_cost}")
    if state.within_budget:
        print("Trip is within budget")
    else:
        print("Trip exceeds budget")

    return state
    