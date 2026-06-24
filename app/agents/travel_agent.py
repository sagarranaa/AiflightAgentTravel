from app.llm.client import ask_llm
from app.parsers.trip_parser import parse_trip_response
from app.prompts.travel_prompt import TRAVEL_SYSTEM_PROMPT


def create_trip(user_request: str):
    """
    Generate a trip plan using AI.
    """

    messages = [
        {
            "role": "system",
            "content": TRAVEL_SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_request
        }
    ]

    # Ask the LLM
    response = ask_llm(messages)

    print("\n=== RAW LLM RESPONSE ===\n")
    print(response)

    # Convert JSON -> TripPlan
    trip = parse_trip_response(response)

    return trip