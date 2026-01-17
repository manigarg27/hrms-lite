from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from ..database import SessionLocal
from ..schemas import AttendanceCreate, AttendanceResponse
from ..models import Attendance, Employee
from ..crud import create_attendance, get_attendance_for_employee
from ..logging_config import get_logger

logger = get_logger("attendance")

router = APIRouter(prefix="/attendance", tags=["Attendance"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AttendanceResponse, status_code=201)
def mark_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    try:
        employee = db.query(Employee).filter(
            Employee.id == attendance.employee_id
        ).first()

        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        existing = db.query(Attendance).filter(
            Attendance.employee_id == attendance.employee_id,
            Attendance.date == attendance.date
        ).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Attendance already marked for this date"
            )

        return create_attendance(db, attendance)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Mark attendance error: {e}")
        raise HTTPException(status_code=500, detail="Failed to mark attendance")


@router.get("/{employee_id}", response_model=list[AttendanceResponse])
def get_attendance(employee_id: UUID, db: Session = Depends(get_db)):
    try:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        return get_attendance_for_employee(db, employee_id)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Fetch attendance error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch attendance")
