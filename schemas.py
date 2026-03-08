# -------------------------
# schemas.py
# -------------------------
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


# -------------------------
# STUDENT SCHEMAS
# -------------------------
class StudentBase(BaseModel):
    name: str
    email: EmailStr


class StudentCreate(StudentBase):
    password: str


class StudentLogin(BaseModel):
    email: EmailStr
    password: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True


# -------------------------
# JOB SCHEMAS
# -------------------------
class JobBase(BaseModel):
    title: str
    effort: int   # effort acts as Compute Units (Ci) in priority formula
    deadline: date  # used to compute Urgency = Deadline - Today
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


# -------------------------
# STUDENT SCHEMAS
# -------------------------

class StudentBase(BaseModel):
    name: str
    email: EmailStr


class StudentCreate(StudentBase):
    password: str


class StudentLogin(BaseModel):
    email: EmailStr
    password: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True


# -------------------------
# JOB SCHEMAS
# -------------------------

class JobBase(BaseModel):
    title: str
    effort: int
    deadline: date


class JobCreate(JobBase):
    pass


class JobUpdate(BaseModel):
    title: Optional[str] = None
    effort: Optional[int] = None
    deadline: Optional[date] = None
    status: Optional[str] = None


class Job(JobBase):
    id: int
    status: str
    attended_day: Optional[date] = None

    class Config:
        from_attributes = True

class JobCreate(JobBase):
    pass


class JobUpdate(BaseModel):
    title: Optional[str] = None
    effort: Optional[int] = None
    deadline: Optional[date] = None
    status: Optional[str] = None


class Job(JobBase):
    id: int
    status: str
    attended_day: Optional[date] = None

    class Config:
        from_attributes = True