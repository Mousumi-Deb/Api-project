
#  Now create Basemodel for doctor and nurse
from pydantic import BaseModel

# below is the pydanitic model for doctor and nurse which is coming from BaseModel
# creating a doctor class


class Doctor(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    age: int


class UpdateDoctor(BaseModel):
    id: int
    first_name: str = None
    last_name: str = None
    age: int = None

# creating a nurse class


class NurseLog(BaseModel):
    id: int = None
    nurse_name: str
    working_hour: int
    room_num: int
    doctor_id: int

# update nurse class


class UpdateNurseLog(BaseModel):
    id: int
    nurse_name: str = None
    working_hour: int = None
    room_num: int = None
    doctor_id: int = None
