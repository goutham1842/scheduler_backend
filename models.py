# -------------------------
# models.py
# -------------------------
from sqlalchemy import Column, Integer, String, Date
from database import Base


# -------------------------
# STUDENT TABLE
# -------------------------
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    password = Column(String, nullable=False)


# -------------------------
# JOB TABLE
# -------------------------
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    effort = Column(Integer, nullable=False)

    deadline = Column(Date, nullable=False)

    status = Column(String, default="pending")

    attended_day = Column(Date, nullable=True)