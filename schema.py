from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    # Não foi colocado o "None" por causa de um bug.
    # last_name: str = None 
    last_name: str
    age: int

    class Config:
            orm_mode = True