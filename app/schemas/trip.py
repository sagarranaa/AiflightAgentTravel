from pydantic import BaseModel, ConfigDict

class TripPlan(BaseModel):
      destination:str
      days:int
      budget:int
      hotel_budget:int
      activities:list[str]

      model_config = ConfigDict(
        extra="forbid"
    )