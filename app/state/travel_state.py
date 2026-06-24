from typing import Optional
from pydantic import BaseModel


class TravelState(BaseModel):
    # User inputs
    destination: str
    days: int
    budget: int

    # Data added by agents later
    flight: Optional[dict] = None
    hotel: Optional[dict] = None

    # Calculated values
    total_cost: Optional[int] = None
    within_budget: Optional[bool] = None