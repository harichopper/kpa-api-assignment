from pydantic import BaseModel

class FormCreate(BaseModel):
    name: str
    email: str
    phone: str
    location: str

class FormOut(FormCreate):
    id: int

    class Config:
        orm_mode = True
