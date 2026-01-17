
# HRMS Lite Backend

## Overview

The backend is built using **FastAPI** and exposes RESTful APIs for:

- Employee CRUD operations
- Attendance management

Data is persisted using a relational database (SQLite by default). All endpoints include **basic validations** and return meaningful HTTP responses.


---

## API Endpoints

### Employee

| Method | Endpoint             | Description                 |
| ------ | ------------------  | --------------------------- |
| POST   | /employees/          | Add a new employee          |
| GET    | /employees/          | List all employees          |
| DELETE | /employees/{id}/     | Delete an employee          |

### Attendance

| Method | Endpoint                  | Description                     |
| ------ | ------------------------- | ------------------------------- |
| POST   | /attendance/              | Mark attendance for an employee |
| GET    | /attendance/{employee_id} | Get attendance records          |

---

## Setup Locally

1. Navigate to backend:

```bash
cd hrms-lite/backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload
