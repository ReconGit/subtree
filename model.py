from pydantic import BaseModel

class Model(BaseModel):
    name: str
    value: int

    class Config:
        orm_mode = True
