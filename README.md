# hrms-lite
**Lightweight Human Resource Management System (HRMS Lite)**

--
## Live Application
[https://hrms-lite-five.vercel.app](https://hrms-lite-five.vercel.app)  

--

## Project Overview

HRMS Lite is a lightweight Human Resource Management System designed to allow an admin to:

- Manage employee records
- Track daily attendance

The system simulates a basic internal HR tool with essential HR operations, focusing on clean UI, stable functionality, and production readiness.

This project was built as a full-stack assignment to demonstrate end-to-end development skills, including frontend, backend, database design, validation, and deployment.

---

## Tech Stack

| Layer       | Technology           |
| ----------- | ------------------ |
| Frontend    | React, Vite, Axios  |
| Backend     | FastAPI, Python     |
| Database    | SQLite (default)    |
| Deployment  | Vercel (Frontend), Render (Backend) |

---

## Project Structure

hrms-lite/
│
├─ backend/ # FastAPI backend
├─ frontend/ # React frontend
└─ README.md # Project overview


---

## Features

### Employee Management
- Add employee (ID, Full Name, Email, Department)
- View all employees
- Delete employee

### Attendance Management
- Mark attendance (Date, Status)
- View attendance per employee
- Optional: Filter by date / total present days

---

## Assumptions & Limitations
- Single admin user (no authentication)
- No leave management, payroll, or advanced HR features
- Core features focus on CRUD for employees and attendance

---

Follow backend and frontend README.md for setup instructions.


