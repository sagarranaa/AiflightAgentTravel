import json

from app.schemas.trip import TripPlan


def parse_trip_response(response: str) -> TripPlan:
    """
    Clean LLM response and convert it into TripPlan.
    """
    # Remove markdown code fences
    cleaned_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )
    print("\nCleaned Response:")
    print(cleaned_response)
    # Convert JSON string into Python dictionary
    data = json.loads(cleaned_response)
    # Validate with Pydantic
    trip = TripPlan(**data)

    return trip