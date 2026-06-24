import os
import sys

# Add project root to Python path
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import streamlit as st

from app.state.travel_state import TravelState
from app.graph.travel_graph import travel_graph


# Page configuration
st.set_page_config(
    page_title="AI Travel Agent",
    page_icon="✈️",
    layout="centered"
)


# Title
st.title("✈️ AI Travel Planner")
st.write("Plan your trip using LangGraph Multi-Agent System")


# User inputs
destination = st.text_input(
    "Enter Destination",
    placeholder="Example: Goa"
)

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=2
)

budget = st.number_input(
    "Enter Budget (₹)",
    min_value=1000,
    step=1000,
    value=10000
)


# Button
if st.button("Plan My Trip"):

    if not destination.strip():
        st.error("Please enter a destination.")

    else:
        with st.spinner("🤖 AI Agents are planning your trip..."):

            try:
                # Create state
                state = TravelState(
                    destination=destination,
                    days=days,
                    budget=budget
                )

                # Run LangGraph
                result = travel_graph.invoke(
                    state.model_dump()
                )

                # Success
                st.success("🎉 Trip Planned Successfully!")

                # Trip details
                st.header("📍 Trip Details")

                st.write(f"Destination: {result['destination']}")
                st.write(f"Days: {result['days']}")
                st.write(f"Budget: ₹{result['budget']}")

                # Flight details
                if result.get("flight"):
                    st.header("✈️ Flight Details")

                    flight = result["flight"]

                    st.write(
                        f"""
Airline: {flight['airline']}

From: {flight['departure']}

To: {flight['destination']}

Price: ₹{flight['price']}
"""
                    )

                # Hotel details
                if result.get("hotel"):
                    st.header("🏨 Hotel Details")

                    hotel = result["hotel"]

                    st.write(
                        f"""
Hotel: {hotel['name']}

Location: {hotel['location']}

Nights: {hotel['nights']}

Price: ₹{hotel['price']}
"""
                    )

                # Budget summary
                st.header("💰 Budget Summary")

                st.write(
                    f"Total Cost: ₹{result['total_cost']}"
                )

                if result.get("within_budget"):
                    st.success(
                        "✅ Trip is within budget"
                    )
                else:
                    st.error(
                        "❌ Trip exceeds budget"
                    )

                # Show raw JSON (optional)
                with st.expander("View Complete Travel State"):
                    st.json(result)

            except Exception as e:
                st.error(
                    f"Something went wrong: {e}"
                )