from pydantic import BaseModel

class TestEntry(BaseModel):
    topic: str
    summary: str

# Add more classes as needed for your application here:
