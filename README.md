# Student Job Command Center

A Smart Job Scheduling System for students to manage tasks based on priority and urgency.
MY WEBSITE LINK IS : https://scheduler-backend-phi.vercel.app

## Features
- Student Login / Signup
- Job Creation
- Smart Scheduling Algorithm
- Priority and Urgency Calculation
- Job Dashboard

## Installation

Clone the repository:

git clone https://github.com/yourusername/scheduler_backend.git

Move into project folder:

cd scheduler_backend

Install dependencies:

pip install -r requirements.txt

## Usage

Run the FastAPI server:

uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| POST | /signup | Create student account |
| POST | /login | Student login |
| POST | /jobs | Create job |
| GET | /jobs | Get all jobs |
| GET | /schedule | Get scheduled jobs |

## Setup

Make sure Python 3.9+ is installed.

Install dependencies:

pip install fastapi uvicorn sqlalchemy pydantic

## Author

Goutham Naidu Bali
