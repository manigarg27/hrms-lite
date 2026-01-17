from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import date
from enum import Enum


class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str


class EmployeeResponse(EmployeeCreate):
    id: UUID

    class Config:
        orm_mode = True


class AttendanceStatus(str, Enum):
    Present = "Present"
    Absent = "Absent"


class AttendanceCreate(BaseModel):
    employee_id: UUID
    date: date
    status: AttendanceStatus


class AttendanceResponse(AttendanceCreate):
    id: UUID

    class Config:
        orm_mode = True
