# -------------------------
# main.py
# -------------------------
from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import statistics
from typing import List

from database import engine, SessionLocal
import models, schemas

# -------------------------
# APP
# -------------------------
app = FastAPI(title="Student Job Command Center")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Create tables
# -------------------------
models.Base.metadata.create_all(bind=engine)

# -------------------------
# DB Dependency
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# AUTHENTICATION
# -------------------------

@app.post("/signup")
def signup(student: schemas.StudentCreate, db: Session = Depends(get_db)):

    existing = db.query(models.Student).filter(models.Student.email == student.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_student = models.Student(
        name=student.name,
        email=student.email,
        password=student.password
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Signup successful",
        "student_id": new_student.id
    }


@app.post("/login")
def login(student: schemas.StudentLogin, db: Session = Depends(get_db)):

    db_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="User not found")

    if db_student.password != student.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {
        "message": "Login successful",
        "student_id": db_student.id,
        "name": db_student.name
    }

# -------------------------
# Seed Jobs
# -------------------------
@app.on_event("startup")
def seed_jobs_on_startup():
    db = SessionLocal()
    try:
        if db.query(models.Job).count() == 0:
            jobs_list = [
               {"title": "Internship at ABC Corp", "effort": 5, "deadline": date(2026, 3, 7)},
    {"title": "Online Research Project", "effort": 3, "deadline": date(2026, 3, 5)},
    {"title": "Freelance Design Task", "effort": 8, "deadline": date(2026, 3, 10)},
    {"title": "Open Source Contribution", "effort": 2, "deadline": date(2026, 3, 6)},
    {"title": "Hackathon Challenge", "effort": 7, "deadline": date(2026, 3, 8)},
    
    # Additional tasks
    {"title": "Complete Python Course Assignment", "effort": 4, "deadline": date(2026, 3, 4)},
    {"title": "Team Meeting Preparation", "effort": 2, "deadline": date(2026, 3, 3)},
    {"title": "Database Design Document", "effort": 6, "deadline": date(2026, 3, 9)},
    {"title": "Client Presentation Slides", "effort": 5, "deadline": date(2026, 3, 11)},
    {"title": "Code Review for Project X", "effort": 3, "deadline": date(2026, 3, 12)},
    {"title": "Write Technical Documentation", "effort": 7, "deadline": date(2026, 3, 13)},
    {"title": "Fix Critical Bug in Production", "effort": 4, "deadline": date(2026, 3, 2)},
    {"title": "Update Resume and Portfolio", "effort": 3, "deadline": date(2026, 3, 15)},
    {"title": "Prepare for Job Interview", "effort": 8, "deadline": date(2026, 3, 14)},
    {"title": "Mobile App UI Design", "effort": 9, "deadline": date(2026, 3, 18)},
    {"title": "Backend API Development", "effort": 10, "deadline": date(2026, 3, 20)},
    {"title": "Write Unit Tests", "effort": 5, "deadline": date(2026, 3, 16)},
    {"title": "Deploy Application to Server", "effort": 4, "deadline": date(2026, 3, 17)},
    {"title": "Create Wireframes for New Feature", "effort": 6, "deadline": date(2026, 3, 19)},
    {"title": "Conduct User Testing", "effort": 7, "deadline": date(2026, 3, 21)},
    {"title": "Analyze Survey Results", "effort": 5, "deadline": date(2026, 3, 22)},
    {"title": "Optimize Database Queries", "effort": 8, "deadline": date(2026, 3, 23)},
    {"title": "Learn React Framework", "effort": 12, "deadline": date(2026, 3, 30)},
    {"title": "Build Portfolio Website", "effort": 15, "deadline": date(2026, 3, 28)},
    {"title": "Write Blog Post on Tech Trends", "effort": 4, "deadline": date(2026, 3, 24)},
    {"title": "Record Coding Tutorial Video", "effort": 6, "deadline": date(2026, 3, 25)},
    {"title": "Participate in Online Webinar", "effort": 3, "deadline": date(2026, 3, 26)},
    {"title": "Complete Certification Exam", "effort": 10, "deadline": date(2026, 3, 29)},
    {"title": "Organize Study Group Session", "effort": 4, "deadline": date(2026, 3, 27)},
    {"title": "Create Project Roadmap", "effort": 5, "deadline": date(2026, 3, 31)},
    {"title": "Update LinkedIn Profile", "effort": 2, "deadline": date(2026, 3, 1)},
    {"title": "Networking Event Attendance", "effort": 4, "deadline": date(2026, 4, 2)},
    {"title": "Write Cover Letter for Job App", "effort": 3, "deadline": date(2026, 4, 1)},
    {"title": "Practice Coding Challenges", "effort": 8, "deadline": date(2026, 4, 3)},
    {"title": "Contribute to Team Wiki", "effort": 3, "deadline": date(2026, 3, 18)},
    {"title": "Review Pull Requests", "effort": 5, "deadline": date(2026, 3, 19)},
    {"title": "Setup Development Environment", "effort": 4, "deadline": date(2026, 3, 2)},
    {"title": "Attend Scrum Meeting", "effort": 1, "deadline": date(2026, 3, 3)},
    {"title": "Prepare Sprint Demo", "effort": 6, "deadline": date(2026, 3, 20)},
    {"title": "Research New Technologies", "effort": 7, "deadline": date(2026, 3, 22)},
    {"title": "Create Data Visualization", "effort": 5, "deadline": date(2026, 3, 23)},
    {"title": "Write API Documentation", "effort": 4, "deadline": date(2026, 3, 24)},
    {"title": "Fix UI Responsiveness Issues", "effort": 6, "deadline": date(2026, 3, 25)},
    {"title": "Implement Authentication System", "effort": 9, "deadline": date(2026, 3, 27)},
    {"title": "Conduct Code Refactoring", "effort": 7, "deadline": date(2026, 3, 26)},
    {"title": "Write User Manual", "effort": 5, "deadline": date(2026, 3, 28)},
    {"title": "Prepare Monthly Report", "effort": 4, "deadline": date(2026, 3, 30)},
    {"title": "Backup Important Files", "effort": 2, "deadline": date(2026, 3, 15)},
    {"title": "Clean Up Old Branches", "effort": 2, "deadline": date(2026, 3, 12)},
    {"title": "Update Dependencies", "effort": 3, "deadline": date(2026, 3, 14)}
            ]
            for job in jobs_list:
                db_job = models.Job(
                    title=job["title"],
                    effort=job["effort"],
                    deadline=job["deadline"],
                    status="upcoming",
                    attended_day=None
                )
                db.add(db_job)
            db.commit()
    finally:
        db.close()

# -------------------------
# CREATE JOB
# -------------------------
@app.post("/jobs", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = models.Job(
        title=job.title,
        effort=job.effort,
        deadline=job.deadline,
        status="upcoming",
        attended_day=None
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# -------------------------
# GET JOBS
# -------------------------
@app.get("/jobs", response_model=List[schemas.Job])
def get_jobs(db: Session = Depends(get_db)):
    today = date.today()
    jobs = db.query(models.Job).all()

    for job in jobs:
        if job.status == "upcoming" and today > job.deadline:
            job.status = "missed"

    db.commit()
    return jobs

# -------------------------
# SMART SUGGEST (GREEDY)
# -------------------------
@app.get("/jobs/smart_suggest", response_model=List[schemas.Job])
def smart_suggest(n: int = Query(3), db: Session = Depends(get_db)):

    today = date.today()

    jobs = db.query(models.Job).filter(models.Job.status == "upcoming").all()

    def priority(job):

        # CORE IDEA
        # Urgency = Deadline - Today
        urgency = (job.deadline - today).days

        urgency = max(urgency, 0)

        effort = job.effort

        # PRIORITY FORMULA
        priority_value = (1 / (urgency + 1)) + (1 / effort)

        return priority_value

    jobs.sort(key=priority, reverse=True)

    return jobs[:n]

# -------------------------
# SELECT JOBS
# -------------------------
@app.post("/jobs/select", response_model=List[schemas.Job])
def select_jobs(
    job_ids: List[int],
    daily_limit: int = Query(...),
    db: Session = Depends(get_db)
):

    if len(job_ids) > daily_limit:
        raise HTTPException(status_code=400, detail=f"Daily capacity exceeded! Limit is {daily_limit}")

    jobs = db.query(models.Job).filter(models.Job.id.in_(job_ids)).all()

    today = date.today()

    for job in jobs:

        if job.status != "upcoming":
            raise HTTPException(status_code=400, detail=f"Job {job.id} is not available")

        job.status = "attended"
        job.attended_day = today

    db.commit()

    return jobs

# -------------------------
# PROFILE DASHBOARD
# -------------------------
@app.get("/profile")
def profile_dashboard(db: Session = Depends(get_db)):

    attended = db.query(models.Job).filter(models.Job.status == "attended").count()
    missed = db.query(models.Job).filter(models.Job.status == "missed").count()
    upcoming = db.query(models.Job).filter(models.Job.status == "upcoming").count()

    if attended > 20:
        level = "Lead Engineer"

    elif attended > 10:
        level = "Senior Developer"

    elif attended > 5:
        level = "Junior Developer"

    else:
        level = "Intern"

    return {
        "attended": attended,
        "missed": missed,
        "upcoming": upcoming,
        "level": level
    }

# -------------------------
# SMOOTHING SCORE
# -------------------------
@app.get("/analytics/smoothing")
def smoothing_score(db: Session = Depends(get_db)):

    jobs = db.query(models.Job).filter(models.Job.status == "attended").all()

    if not jobs:
        return {"smoothing_score": 0}

    daily_counts = {}

    for job in jobs:
        if job.attended_day:
            daily_counts[job.attended_day] = daily_counts.get(job.attended_day, 0) + 1

    counts = list(daily_counts.values())

    if len(counts) < 2:
        return {"smoothing_score": 100}

    variance = statistics.pstdev(counts)

    score = max(0, 100 - variance * 15)

    return {"smoothing_score": round(score, 2)}

# -------------------------
# ANALYTICS
# -------------------------
@app.get("/analytics")
def analytics_dashboard(db: Session = Depends(get_db)):

    total = db.query(models.Job).count()
    attended = db.query(models.Job).filter(models.Job.status == "attended").count()

    success_rate = (attended / total) * 100 if total > 0 else 0

    placement_probability = min(95, success_rate * 0.85)

    return {
        "success_rate": round(success_rate, 2),
        "placement_probability": round(placement_probability, 2)
    }