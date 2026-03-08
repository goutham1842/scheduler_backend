# -------------------------
# schemas.py
# -------------------------

from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional


# -------------------------
# STUDENT SCHEMAS
# -------------------------

class StudentBase(BaseModel):
    name: str
    email: EmailStr


# Used when creating a student (signup)
class StudentCreate(StudentBase):
    password: str


# Used for login
class StudentLogin(BaseModel):
    email: EmailStr
    password: str


# Used when updating student details
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


# Response model
class StudentResponse(StudentBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


# -------------------------
# JOB SCHEMAS
# -------------------------

class JobBase(BaseModel):
    title: str
    effort: int = Field(..., gt=0, description="Effort required for the job")
    deadline: date = Field(..., description="Deadline (YYYY-MM-DD)")


# Create job
class JobCreate(JobBase):
    pass


# Update job
class JobUpdate(BaseModel):
    title: Optional[str] = None
    effort: Optional[int] = Field(None, gt=0)
    deadline: Optional[date] = None
    status: Optional[str] = None


# Response model used in APIs
class Job(JobBase):
    id: int
    status: str
    attended_day: Optional[date] = None

    class Config:
        from_attributes = True