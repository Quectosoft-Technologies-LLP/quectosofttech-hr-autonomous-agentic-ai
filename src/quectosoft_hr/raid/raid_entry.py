from pydantic import BaseModel, Field
class RAIDEntry(BaseModel):
    category: str
    description: str
    likelihood: int = Field(ge=1, le=5)
    impact: int = Field(ge=1, le=5)
    owner: str
