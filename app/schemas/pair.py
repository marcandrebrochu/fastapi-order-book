from pydantic import BaseModel

class Pair(BaseModel):
    base: str
    quote: str