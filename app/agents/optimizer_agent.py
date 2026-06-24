from app.state.travel_state import TravelState


def optimizer_agent(state: TravelState) -> TravelState:
    """
    Try to reduce the trip cost if it exceeds the budget.
    """

    print("\nOptimizer Agent Started...")

    # Reduce hotel cost if available
    if state.hotel:
        old_price = state.hotel["price"]

        # Find a cheaper hotel
        new_price = old_price - 2000

        # Make sure price does not go below a minimum value
        if new_price < 3000:
            new_price = 3000

        state.hotel["price"] = new_price

        print(
            f"Hotel price reduced from ₹{old_price} to ₹{new_price}"
        )

    # Reduce flight cost if available
    if state.flight:
        old_price = state.flight["price"]

        # Find a cheaper flight
        new_price = old_price - 1000

        if new_price < 2500:
            new_price = 2500

        state.flight["price"] = new_price

        print(
            f"Flight price reduced from ₹{old_price} to ₹{new_price}"
        )

    print("Optimization completed")

    return state