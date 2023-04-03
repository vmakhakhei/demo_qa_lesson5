from dataclasses import dataclass
from enum import Enum


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'

class Subjects(Enum):
    maths = "Maths"
    chemistry = "Chemistry"
    english = "English"
    biology = "Biology"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: str
    hobbies: str
    name_picture: str
    adress: str
    state: str
    city: str
