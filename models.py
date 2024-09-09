from pydantic import BaseModel, Field, EmailStr, ValidationInfo, field_validator
from enum import Enum
import dataclasses
from error import *

#Using String Enum for the gender of student
class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

#Using Dataclass for the teacher data
@dataclasses.dataclass
class Teacher:
    id: int
    name: str
    subjects: str

#Using pydantic basemodel for the student data
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    address: str = Field(..., min_length=10, max_length=50)
    sex: Gender

    #Validating the address of student using field validator
    @field_validator('address')
    def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            is_alphanumeric = v.replace(' ', '').isalnum()
            assert is_alphanumeric, f'{info.field_name} must be alphanumeric'
        return v

    #Validating the age of student using field validator
    @field_validator('age')
    @classmethod
    def check_age(cls, v: int) -> int:
        if v < 18:
            raise InvalidAgeError(v)
        return v

    #Validating the name of student using field validator
    @field_validator('name')
    def check_name(cls, v: str) -> str:
        if not v.isalpha() or len(v) < 3: 
            raise InvalidNameError(v)
        return v
